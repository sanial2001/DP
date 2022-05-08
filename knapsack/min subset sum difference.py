def subsetsum(arr, S, N):
    t = [[0 for j in range(S + 1)] for i in range(N + 1)]
    vec = []

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

    for val in t:
        print(val)
    if S % 2 != 0:
        for i in range((S + 1) // 2):
            if t[N][i]:
                vec.append(i)
    else:
        for i in range((S + 1) // 2 + 1):
            if t[N][i]:
                vec.append(i)

    return vec


def min_dif(arr, n):
    max_sum = 0
    for ele in arr:
        max_sum = max_sum + ele

    vec = subsetsum(arr, max_sum, n)
    most_min = 10000
    for i in vec:
        #print(i)
        most_min = min(most_min, max_sum - 2 * i)
    return most_min


if __name__ == '__main__':
    info = {
        'arr': [10, 8],
        'n': 2
    }
    print(min_dif(info['arr'], info['n']))
