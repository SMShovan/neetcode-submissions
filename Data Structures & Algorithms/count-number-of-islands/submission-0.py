class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r, c):
            visit.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    neir, neic = row + dr, col + dc

                    if (neir in range(rows) and neic in range(cols) and grid[neir][neic] == "1" and (neir, neic) not in visit):
                        q.append((neir, neic))
                        visit.add((neir, neic))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row, col)
                    island += 1
        
        return island
