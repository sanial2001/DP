def lrs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m-1] == y[n-1] and m != n:
        return 1 + lrs(x, y, m-1, n-1)
    else:
        return max(lrs(x, y, m, n-1), lrs(x, y, m-1, n))


def lrs_dp(x, y, M, N):
    t = [[-1 for y in range(N+1)] for x in range(M+1)]

    for i in range(M+1):
        for j in range(N+1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for m in range(1, M+1):
        for n in range(1, N+1):
            if x[m-1] == y[n-1] and m != n:
                t[m][n] = 1 + t[m-1][n-1]
            else:
                t[m][n] = max(t[m][n-1], t[m-1][n])

    return t[M][N]


if __name__=='__main__':
    info = {
        'str1': 'abdeabdc',
        'm': 8
    }
    print(lrs_dp(info['str1'], info['str1'], info['m'], info['m']))
