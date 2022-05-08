class Solution:
    def solve(self, maze, row, col, visited, dest):
        if row < 0 or row == len(maze) or col < 0 or col == len(maze[0]) or visited[row][col] == True or maze[row][col] == 1:
            return
        visited[row][col] = True
        self.solve(maze, row-1, col, visited, dest)
        self.solve(maze, row, col-1, visited, dest)
        self.solve(maze, row+1, col, visited, dest)
        self.solve(maze, row, col+1, visited, dest)
        if row == dest[0] and col == dest[1]:
            print('reach')
            self.ans = True
        visited[row][col] = False

    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.ans = False
        self.solve(maze, start[0], start[1], visited, destination)
        print(self.ans)


if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    Solution().hasPath(maze, [0, 4], [4, 4])
