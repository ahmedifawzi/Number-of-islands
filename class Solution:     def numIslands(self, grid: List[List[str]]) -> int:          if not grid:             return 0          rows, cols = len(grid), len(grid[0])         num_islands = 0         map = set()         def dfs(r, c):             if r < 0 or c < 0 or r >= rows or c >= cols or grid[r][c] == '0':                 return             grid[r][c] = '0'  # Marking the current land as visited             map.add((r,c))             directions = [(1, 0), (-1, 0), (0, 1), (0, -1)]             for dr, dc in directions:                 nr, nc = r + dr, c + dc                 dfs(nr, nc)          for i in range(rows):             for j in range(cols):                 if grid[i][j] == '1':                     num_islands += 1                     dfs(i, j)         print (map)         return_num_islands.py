class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        map = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # Marking the current land as visited
            map.add((r,c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        print (map)
        return num_islands
