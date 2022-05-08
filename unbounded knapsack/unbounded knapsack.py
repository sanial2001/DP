def unbounded_knapsack(wt, val, w, n):
    if w == 0 or n == 0:
        return 0

    if wt[n-1] <= w:
        return max(val[n-1] + unbounded_knapsack(wt, val, w-wt[n-1], n),
                   unbounded_knapsack(wt, val, w, n-1))
    elif wt[n-1] > w:
        return unbounded_knapsack(wt, val, w, n-1)


def unbounded_knapsack_dp(wt, val, W, N):
    t = [[-1 for y in range(W+1)] for x in range(N+1)]

    for n in range(N+1):
        for w in range(W+1):
            if n == 0 or w == 0:
                t[n][w] = 0

    for n in range(1, N+1):
        for w in range(1, W+1):
            if wt[n-1] <= w:
                t[n][w] = max(val[n-1] + t[n][w-wt[n-1]], t[n-1][w])
            elif wt[n-1] > w:
                t[n][w] = t[n-1][w]

    return t[N][W]


if __name__=='__main__':
    info = {
        'weight': [2, 3, 1, 4],
        'value': [2, 6, 2, 10],
        'tot_wt': 6,
        'n': 4
    }
    print('profit : {}'.format(unbounded_knapsack_dp(info['weight'],
                                                      info['value'],
                                                      info['tot_wt'],
                                                      info['n'])))
