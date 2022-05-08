def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m-1] == y[n-1]:
        return 1 + lcs(x, y, m-1, n-1)
    else:
        return max(lcs(x, y, m, n-1), lcs(x, y, m-1, n))


def lcs_dp(x, y, M, N):
    t = [[-1 for y in range(N+1)] for x in range(M+1)]

    for i in range(M+1):
        for j in range(N+1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for m in range(1, M+1):
        for n in range(1, N+1):
            if x[m-1] == y[n-1]:
                t[m][n] = 1 + t[m-1][n-1]
            else:
                t[m][n] = max(t[m][n-1], t[m-1][n])

    return t[M][N]


def lps(x, m):
    y = x[::-1]
    n = len(y)
    return lcs_dp(x, y, m, n)


def min_deletion_palindrome(x, m):
    return m - lps(x, m)


if __name__ == '__main__':
    info = {
        'str1': 'abccbe',
        'm': 6,
    }
    print(min_deletion_palindrome(info['str1'], info['m']))
