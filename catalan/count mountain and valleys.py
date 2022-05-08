def solve(n):
    t = [0 for _ in range(n+1)]
    t[0], t[1] = 1, 1

    for i in range(2, n+1):
        j, k = 0, i-1
        while j < i and k >= 0:
            t[i] = t[i] + t[j]*t[k]
            j, k = j+1, k-1

    print(t[n])


if __name__ == '__main__':
    solve(3)
