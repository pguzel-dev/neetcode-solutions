# derived from Graph Valid Tree
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build an adjacency list for the undirected graph
        graph = {i: [] for i in range(n)}

        # Add each edge in both directions
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Track nodes we have already visited
        visited = set()
        count = 0

        def dfs(node):
            # Stop if this node was already explored
            if node in visited:
                return

            # Mark the current node as visited
            visited.add(node)

            # Visit all neighboring nodes
            for nei in graph[node]:
                dfs(nei)

        # Start a DFS from every unvisited node
        for node in range(n):
            if node not in visited:
                dfs(node)

                # Each new DFS means we found a new component
                count += 1

        return count