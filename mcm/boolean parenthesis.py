'''def solve_recursion(str, i, j, isTrue):
    if i > j:
        return False
    elif i == j:
        if isTrue:
            return True
        else:
            return False

    ans = 0
    for k in range(i+1, j, 2):
        lt = solve(str, i, k-1, True)
        lf = solve(str, i, k-1, False)
        rt = solve(str, k+1, j, True)
        rf = solve(str, k+1, j, False)

        if str[k] == '&':
            if isTrue:
                ans = ans + lt*rt
            else:
                ans = ans + lt*rf + lf*rt + lf*rf
        elif str[k] == '|':
            if isTrue:
                ans = ans + lt*rt + lt*rf + lf*rt
            else:
                ans = ans + lf*rf
        elif str[k] == '^':
            if isTrue:
                ans = ans + lt*rf + lf*rt
            else:
                ans = ans + lt*rt + lf*rf
    return ans
'''


def solve(str1, str2):
    n = len(str1)
    t = [[0 for _ in range(n)] for _ in range(n)]
    f = [[0 for _ in range(n)] for _ in range(n)]

    for g in range(n):
        i = 0
        for j in range(g, n):
            if g == 0:
                if str1[j] == 'T':
                    t[i][j] = 1
                    f[i][j] = 0
                else:
                    t[i][j] = 0
                    f[i][j] = 1
            else:
                for k in range(i, j):
                    lt = t[i][k]
                    lf = f[i][k]
                    rt = t[k+1][j]
                    rf = f[k+1][j]
                    if str2[k] == '&':
                        t[i][j] = t[i][j] + lt*rt
                        f[i][j] = f[i][j] + lt*rf + lf*rt + lf*rf
                    elif str2[k] == '|':
                        t[i][j] = t[i][j] + lt*rt + lf*rt + lt*rf
                        f[i][j] = f[i][j] + lf*rf
                    elif str2[k] == '^':
                        t[i][j] = t[i][j] + lt*rf + lf*rt
                        f[i][j] = f[i][j] + lt*rt + lf*rf
            i = i+1

    for val in t:
        print(val)


if __name__ == '__main__':
    str1 = 'TFTF'
    str2 = '&|^'
    print(solve(str1, str2))
