# suggested solution but the time is about the same
class Solution:
    def validTree(self, n, edges):
        # Empty graph is considered valid
        if not n:
            return True

        # Build adjacency list for the undirected graph
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Track visited nodes to detect cycles
        visit = set()

        def dfs(i, prev):
            # If already visited, a cycle exists
            if i in visit:
                return False

            # Mark current node as visited
            visit.add(i)

            # Visit all neighbors except the parent node
            for j in adj[i]:
                if j == prev:
                    continue

                # If a cycle is found, graph is not a tree
                if not dfs(j, i):
                    return False

            return True

        # Valid tree must be connected and have no cycles
        return dfs(0, -1) and n == len(visit)