def solve(arr):
    n = len(arr)
    t = [[0 for _ in range(n)] for _ in range(2)]
    t[0][0] = arr[0]

    for i in range(1, n):
        t[0][i] = t[1][i-1] + arr[i]
        t[1][i] = max(t[0][i-1], t[1][i-1])

    for val in t:
        print(val)
    print(t[0][n-1])


if __name__ == '__main__':
    arr = [5, 10, 10, 100, 5, 6]
    solve(arr)
