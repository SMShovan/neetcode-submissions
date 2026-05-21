class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))
        
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    neiRow, neiCol = row + dr, col + dc

                    if (neiRow not in range(rows) or neiCol not in range(cols) or grid[neiRow][neiCol] != 1):
                        continue
                    grid[neiRow][neiCol] = 2
                    q.append((neiRow,neiCol))
                    fresh -= 1

            time += 1
        
        return time if fresh == 0 else -1