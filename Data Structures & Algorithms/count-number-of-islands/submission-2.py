class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_root = 0

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        from collections import deque
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if not visited[i][j]:
                        num_root += 1
                        queue = deque()
                        
                        queue.append([i,j])
                        visited[i][j] = True

                        while queue:
                            row, col = queue.popleft()
                            
                            # 그리고 방문 가능하면
                            # 위, 왼, 오른, 아래
                            for di, dj in [(-1, 0), (0, -1), (0, 1), (1,0)]:
                                new_row = row + di
                                new_col = col + dj
                                if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and (grid[new_row][new_col] == "1") and (not visited[new_row][new_col]):
                                    queue.append((new_row, new_col))
                                    visited[new_row][new_col] = True

        return num_root  


                        


        