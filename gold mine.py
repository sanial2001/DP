def solve(matrix, row, col):
    t = [-1 for _ in range(col+1)]
    temp = [val[0] for val in matrix]
    t[0] = max(temp)
    index = temp.index(t[0])

    for i in range(1, col):
        right = matrix[index][i]
        right_up = matrix[index-1][i] if (index-1) >= 0 else -1
        right_down = matrix[index+1][i] if (index+1) < row else -1
        max_icol = max(right, right_up, right_down)
        #print(max_icol)
        t[i] = t[i-1] + max_icol
        temp = [val[i] for val in matrix]
        index = temp.index(max_icol)

    return t[col-1]


def Solve(matrix, m, n):
    t = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        t[i][n-1] = matrix[i][n-1]

    for col in range(n-2, -1, -1):
        for row in range(m):
            if row == 0:
                t[row][col] = matrix[row][col] + max(t[row][col+1], t[row+1][col+1])
            elif row == m-1:
                t[row][col] = matrix[row][col] + max(t[row][col+1], t[row-1][col+1])
            else:
                t[row][col] = matrix[row][col] + max(t[row][col+1], t[row-1][col+1], t[row+1][col+1])

    max_val = -1000
    for i in range(m):
        max_val = max(max_val, t[i][0])
    return max_val


if __name__ == '__main__':
    matrix = [
        [10, 33, 13, 15],
        [22, 21, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 14, 2]
    ]
    print(Solve(matrix, 4, 4))
