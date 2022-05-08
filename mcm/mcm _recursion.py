import sys


def mcm(arr, i, j):
    if i >= j:
        return 0
    min_value = sys.maxsize
    for k in range(i, j):
        temp = mcm(arr, i, k) + mcm(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        print(temp)
        min_value = min(temp, min_value)
        print(min_value, temp)
    return min_value


if __name__ == '__main__':
    info = {
        'arr': [1, 2, 3, 4]
    }
    print(mcm(info['arr'], 1,
              len(info['arr']) - 1))
