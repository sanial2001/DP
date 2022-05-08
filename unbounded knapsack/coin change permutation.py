def solve(arr, n, s):
    t = [0 for _ in range(s+1)]
    t[0] = 1
    for i in range(1, s+1):
        for j in range(n):
            if arr[j] <= i:
                print(arr[j])
                t[i] = 1 + t[i-arr[j]]
            else:
                t[i] = 0
    print(t)


if __name__ == '__main__':
    arr = [2, 3, 4, 5]
    solve(arr, 4, 8)