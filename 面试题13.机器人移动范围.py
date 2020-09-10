# coding = utf-8
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if not m or not n:
            return 0
        
        if not k:
            return 1
        
        def dfs(i, j, si, sj):
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)
