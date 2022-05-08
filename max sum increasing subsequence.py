def solve(arr):
    n = len(arr)
    t = [-1 for _ in range(n)]
    t[0] = arr[0]

    for i in range(1, n):
        j = i - 1
        temp = []
        while j >= 0:
            if arr[i] > arr[j]:
                temp.append(t[j])
            j = j - 1
        if len(temp) > 0:
            t[i] = max(temp) + arr[i]
        else:
            t[i] = arr[i]

    return max(t)


if __name__ == '__main__':
    arr = [1, 100, 2, 100]
    print(solve(arr))
