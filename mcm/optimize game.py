def solve(arr):
    n = len(arr)
    t = [[-1 for _ in range(n)] for _ in range(n)]

    for g in range(n):
        i = 0
        for j in range(g, n):
            if g == 0:
                t[i][j] = arr[i]
            elif g == 1:
                t[i][j] = max(arr[i], arr[j])
            else:
                x1 = arr[i] + min(t[i+2][j], t[i+1][j-1])
                x2 = arr[j] + min(t[i+1][j-1], t[i][j-2])
                t[i][j] = max(x1, x2)
            i = i+1

    print(t[0][n-1])


if __name__ == '__main__':
    arr = [20, 30, 2, 10]
    solve(arr)