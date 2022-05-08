def solve(arr, K):
    N = len(arr)
    t = [[0 for _ in range(N+1)] for _ in range(K+1)]

    for k in range(1, K+1):
        for n in range(1, N+1):
            t[k][n] = t[k][n-1]
            if 0 < arr[n - 1] <= k:
                index_row = k // arr[n-1]
                index_col = n-1
                t[k][n] = t[k][n] + 1 + t[index_row][index_col]

    return t[K][N]


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    k = 10
    print(solve(arr, k))
