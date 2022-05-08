def knapsack(wt, val, W, N):
    t = [[0 for i in range(W+1)] for j in range(N+1)]

    for n in range(N+1):
        for w in range(W+1):
            if n == 0 or w == 0:
                t[n][w] = 0
            elif wt[n-1] <= w:
                t[n][w] = max(val[n-1] + t[n-1][w-wt[n-1]], t[n-1][w])
            elif wt[n-1] > w:
                t[n][w] = t[n-1][w]
    return t[n][w]


if __name__ == '__main__':
    info = {
        'weight': [1, 3, 4, 5],
        'value': [1, 4, 5, 7],
        'total_weight': 7,
        'n': 4
    }
    print('profit : {}'.format(knapsack(info['weight'], info['value'], info['total_weight'], info['n'])))
