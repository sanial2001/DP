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

    return t


def print_lcs(x, y, m, n):
    t = lcs_dp(x, y, m, n)
    match = ''
    i, j = m, n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            match = match + x[i-1]
            i, j = i-1, j-1
        else:
            if t[i][j-1] > t[i-1][j]:
                j = j-1
            else:
                i = i-1

    match = match[::-1]
    return match


if __name__ == '__main__':
    info = {
        'str1': 'abcdgh',
        'str2': 'abedfhr',
        'm': 6,
        'n': 7
    }
    print(print_lcs(info['str1'], info['str2'],
                    info['m'], info['n']))
