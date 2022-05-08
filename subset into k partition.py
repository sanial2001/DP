def solve(N, K):
    t = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(K + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for n in range(1, N + 1):
        for k in range(1, K + 1):
            if k == 1 or n == k:
                t[n][k] = 1
            elif n < k:
                t[n][k] = 0
            else:
                t[n][k] = k * t[n - 1][k] + t[n - 1][k - 1]

    print(t[N][K])


if __name__ == '__main__':
    solve(7, 4)
