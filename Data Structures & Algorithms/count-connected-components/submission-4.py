class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Each node starts as its own parent/component
        par = [i for i in range(n)]

        # Rank stores component size
        rank = [1] * n

        def find(n1):
            # Start from the current node
            res = n1

            # Climb until we reach the root parent
            while res != par[res]:
                # Path compression: shorten future searches
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            # Find root parents of both nodes
            p1, p2 = find(n1), find(n2)

            # Already in the same component
            if p1 == p2:
                return 0
            
            # Attach smaller component under larger component
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            # Successful union reduces component count by 1
            return 1
        
        # Start with n separate components
        res = n

        # Merge components connected by edges
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res