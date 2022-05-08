def solve(a, t, e, x):
    n = len(a[0])
    t1 = [-1 for _ in range(n+1)]
    t2 = [-1 for _ in range(n + 1)]

    t1[0] = e[0] + a[0][0]
    t2[0] = e[1] + a[1][0]
    #print(t1, t2)

    for i in range(1, n+1):
        if i == n:
            t1[i] = t1[i-1] + x[0]
            t2[i] = t2[i-1] + x[1]
        else:
            t1[i] = min(t1[i-1] + a[0][i], t1[i-1] + t[0][i] + a[1][i])
            t2[i] = min(t2[i-1] + a[1][i], t2[i-1] + t[1][i] + a[0][i])

    return min(t1[n], t2[n])


if __name__ == '__main__':
    a = [[4, 5, 3, 2],
         [2, 10, 1, 4]]
    t = [[0, 7, 4, 5],
         [0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]
    print(solve(a, t, e, x))
