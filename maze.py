def solve(maze, row, col, path, ans, visited):
    if row == len(maze) or col == len(maze[0]) or visited[row][col] == True:
        #print(path)
        return
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        #print(path)
        ans.append(path[:])
    #print(path)
    visited[row][col] = True
    solve(maze, row+1, col, path + 'D', ans, visited)
    solve(maze, row, col+1, path + 'R', ans, visited)
    visited[row][col] = False


if __name__ == '__main__':
    maze = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    m, n = len(maze), len(maze[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    path, ans = '', []
    solve(maze, 0, 0, path, ans, visited)
    print(ans)
