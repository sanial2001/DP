def subset_sum(arr, s, n):
    if s == 0:
        return True
    elif n == 0:
        return False

    if arr[n - 1] <= s:
        return subset_sum(arr, s - arr[n - 1], n - 1) or subset_sum(arr, s, n - 1)
    elif arr[n - 1] > s:
        return subset_sum(arr, s, n - 1)


def subset_sum_dp(arr, S, N):
    t = [[0 for x in range(S + 1)] for y in range(N + 1)]

    for i in range(N + 1):
        t[i][0] = True
    for i in range(1, S + 1):
        t[0][i] = False

    for n in range(1, N + 1):
        for s in range(1, S + 1):
            if arr[n - 1] <= s:
                t[n][s] = t[n - 1][s - arr[n - 1]] or t[n - 1][s]
            elif arr[n - 1] > s:
                t[n][s] = t[n - 1][s]

    return True


if __name__ == '__main__':
    info = {
        'arr': [2, 3, 7, 8, 10],
        'sum': 11,
        'n': 5
    }
    print(subset_sum(info['arr'], info['sum'], info['n']))
    print(subset_sum_dp(info['arr'], info['sum'], info['n']))
