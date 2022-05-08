def count_subsetsum(arr, s, n):
    if s == 0:
        return 1
    elif n == 0:
        return 0

    if arr[n-1] <= s:
        return count_subsetsum(arr, s-arr[n-1], n-1) + count_subsetsum(arr, s, n-1)
    elif arr[n-1] > s:
        return count_subsetsum(arr, s, n-1)

def count_subsetsum_dp(arr, S, N):
    t = [[-1 for y in range(S+1)] for x in range(N+1)]

    for i in range(N+1):
        t[i][0] = 1
    for i in range(1, S+1):
        t[0][i] = 0

    for n in range(1, N+1):
        for s in range(1, S+1):
            if arr[n-1] <= s:
                t[n][s] = t[n-1][s-arr[n-1]] + t[n-1][s]
            elif arr[n-1] > s:
                t[n][s] = t[n-1][s]

    return t[N][S]


if __name__ == '__main__':
    info = {
        'arr': [2, 3, 7, 8, 10],
        'sum': 10,
        'n': 5
    }
    print(count_subsetsum(info['arr'], info['sum'], info['n']))
    print(count_subsetsum_dp(info['arr'], info['sum'], info['n']))
