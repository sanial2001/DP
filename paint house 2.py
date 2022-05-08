def solve(a):
    m, n = len(a), len(a[0])
    t = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        t[0][i] = a[0][i]

    temp = []
    for i in range(1, m):
        for j in range(n):
            temp = t[i-1].copy()
            temp.pop(j)
            t[i][j] = min(temp) + a[i][j]

    for val in t:
        print(val)


if __name__ == '__main__':
    m = [[1, 5, 7, 2, 1, 4],
         [5, 8, 4, 3, 6, 1],
         [3, 2, 9, 7, 2, 3],
         [1, 2, 4, 9, 1, 7]]
    solve(m)