def solve(x, y, m, n):
    if m == 0 and n == 0:
        return 0
    if m == 0:
        return n
    if n == 0:
        return m

    if x[m-1] == y[n-1]:
        return solve(x, y, m-1, n-1)
    else:
        delete = solve(x, y, m-1, n)
        replace = solve(x, y, m-1, n-1)
        insert = solve(x, y, m, n-1)
        return 1 + min(delete, replace, insert)


def solve_dp(x, y, M, N):
    t = [[-1 for _ in range(N+1)] for _ in range(M+1)]

    t[0][0] = 0
    for i in range(1, N+1):
        t[0][i] = i
    for i in range(1, M+1):
        t[i][0] = i

    for m in range(1, M+1):
        for n in range(1, N+1):
            if x[m-1] == y[n-1]:
                t[m][n] = t[m-1][n-1]
            else:
                delete = t[m-1][n]
                replace = t[m-1][n-1]
                insert = t[m][n-1]
                t[m][n] = 1 + min(delete, replace, insert)

    return t[M][N]


if __name__ == '__main__':
    x, y = 'geek', 'geek'
    print(solve_dp(x, y, len(x), len(y)))
