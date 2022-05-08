def solve(arr):
    n = len(arr)
    t = [-1 for _ in range(n)]
    t[0] = 1

    for i in range(1, n):
        j = i - 1
        temp = []
        while j >= 0:
            if arr[i] > arr[j]:
                temp.append(t[j])
            j = j - 1
        if len(temp) > 0:
            t[i] = max(temp) + 1
        else:
            t[i] = 1

    for val in t:
        print(val)


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 1]
    solve(arr)
