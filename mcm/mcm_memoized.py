import sys


def mcm(arr):
    n = len(arr)
    t = [[-1 for _ in range(n - 1)] for _ in range(n - 1)]

    for g in range(n - 1):
        i = 0
        for j in range(g, n - 1):
            if g == 0:
                t[i][j] = 0
            elif g == 1:
                t[i][j] = arr[i] * arr[j] * arr[j + 1]
            else:
                min_val = sys.maxsize
                for k in range(i, j):
                    l = t[i][k]
                    r = t[k + 1][j]
                    mm = arr[i] * arr[k + 1] * arr[j + 1]
                    temp = l + r + mm
                    min_val = min(temp, min_val)
                t[i][j] = min_val
            i = i + 1

    return t[0][n - 2]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    print(mcm(arr))
