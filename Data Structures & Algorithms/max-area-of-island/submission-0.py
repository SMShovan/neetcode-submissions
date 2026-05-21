class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maximumArea = float('-inf')

        def dfs(row, col):
            if (row not in range(rows) or col not in range(cols) or grid[row][col] != 1 or (row, col) in visit ):
                return 0
            visit.add((row, col))

            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))
        


        for row in range(rows):
            for col in range(cols):
                maximumArea = max(maximumArea, dfs(row, col))
        
        return maximumArea
