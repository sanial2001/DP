def catalan(n):
    t = [0 for i in range(n + 1)]
    t[0] = t[1] = 1

    for i in range(2, n + 1):
        j, k = 0, i - 1
        while j < i and k >= 0:
            t[i] = t[i] + (t[j] * t[k])
            j, k = j + 1, k - 1

    return t[n]


def solve(n):
    return catalan(n-2)


if __name__ == '__main__':
    print(solve(5))
