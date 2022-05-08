def solve(e, f):
    t = [[-1 for _ in range(f+1)] for _ in range(e+1)]

    for i in range(f+1):
        t[0][i] = None
    for i in range(1, e+1):
        t[i][0] = 0
    for i in range(1, f+1):
        t[1][i] = i
    for i in range(2, e+1):
        t[i][1] = 1

    for i in range(2, e+1):
        for j in range(2, f+1):
            temp = []
            for k in range(j):
                temp.append(max(t[i][j-k-1], t[i-1][k]))
            print(j, temp.index(min(temp)))
            t[i][j] = min(temp) + 1

    for val in t:
        print(val)


def solve_better(k, n):
    e, f = k, n
    t = [[-1 for _ in range(f + 1)] for _ in range(e + 1)]

    for i in range(f + 1):
        t[0][i] = None
    for i in range(1, e + 1):
        t[i][0] = 0
    for i in range(1, f + 1):
        t[1][i] = i
    for i in range(2, e + 1):
        t[i][1] = 1

    for i in range(2, e + 1):
        k = 1
        for j in range(2, f + 1):
            while k < j + 1 and t[i][j - k] > t[i - 1][k - 1]:
                k = k + 1
            t[i][j] = t[i - 1][k - 1] + 1

    for val in t:
        print(val)

    print(t[e][f])


if __name__ == '__main__':
    e, f = 3, 7
    solve_better(e, f)
