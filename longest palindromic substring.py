def solve(s):
    n = len(s)
    t = [[-1 for _ in range(n)] for _ in range(n)]
    start, end = 0, 0

    for g in range(n):
        i = 0
        for j in range(g, n):
            if g == 0:
                t[i][j] = 1
            elif g == 1:
                if s[i] == s[j]:
                    t[i][j] = 1
                    start, end = i, j
                else:
                    t[i][j] = 0
            else:
                if s[i] == s[j] and t[i+1][j-1] == 1:
                    t[i][j] = 1
                    start, end = i, j
                else:
                    t[i][j] = 0
            i = i+1

    print(s[start:end+1])

    '''g = n-1
    flag = 0
    while g >= 0:
        i, j = 0, g
        while j < n:
            if t[i][j] == 1:
                flag = 1
                break
            j = j+1
            i = i+1
        if flag == 1:
            break
        g = g-1

    print(s[i:j+1])
'''


if __name__ == '__main__':
    solve('babad')
