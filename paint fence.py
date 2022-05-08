def paint_fence(n, k):
    t = [-1 for _ in range(n + 1)]
    mod = 1000000007
    t[0], t[1] = k, k * k
    same = k
    diff = k * (k - 1)

    for i in range(2, n):
        same = diff
        diff = t[i - 1] * (k - 1)
        t[i] = (same + diff) % mod

    return t[n-1]


if __name__ == '__main__':
    print(paint_fence(5, 2))
