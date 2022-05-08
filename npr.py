def fact(n):
    t = [-1 for i in range(n+1)]
    t[0] = 1
    for i in range(1, n+1):
        t[i] = i * t[i-1]
    return t[n]


def ncr(n, r):
    if r > n - r:
        r = n - r
    t = [0 for i in range(r+1)]
    t[0] = 1
    #print(t)

    for i in range(1, n+1):
        if i <= r:
            j = i
        else:
            j = r
        while j > 0:
            t[j] = t[j - 1] + t[j]
            j = j - 1

    return t[r]


def npr(n, r):
    return ncr(n, r) * fact(r)


if __name__ == '__main__':
    print(npr(10, 2))
