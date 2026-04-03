class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = {i:[] for i in range(n)}

        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(n, prev):
            if n in visited:
                return False
            visited.add(n)
            for neighbor in adj[n]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, n):
                    return False
            return True

        
        return dfs(0, -1) and len(list(visited)) == n
