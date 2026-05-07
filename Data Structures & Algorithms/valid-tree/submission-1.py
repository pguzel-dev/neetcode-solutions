class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build an undirected adjacency list
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            # If we revisit a node, there is a cycle
            if node in visited:
                return False

            # Mark current node as visited
            visited.add(node)

            # Visit all neighbors
            for nei in graph[node]:
                # Ignore the edge back to the parent
                if nei == parent:
                    continue

                # If a cycle is found, it is not a tree
                if not dfs(nei, node):
                    return False

            return True

        # Start DFS from node 0 and check for cycles
        if not dfs(0, -1):
            return False

        # All nodes must be connected
        return len(visited) == n