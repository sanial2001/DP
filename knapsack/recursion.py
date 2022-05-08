def knapsack(wt, val, tot_wt, n):
    if n == 0 or tot_wt == 0:
        return 0
    if wt[n-1] <= tot_wt:
        return max(val[n-1] + knapsack(wt, val, tot_wt-wt[n-1], n-1), knapsack(wt, val, tot_wt, n-1))
    elif wt[n-1] > tot_wt:
        return knapsack(wt, val, tot_wt, n-1)


if __name__ == '__main__':
    info = {
        'weight': [1, 3, 4, 5],
        'value': [1, 4, 5, 7],
        'total_weight': 7,
        'n': 4
    }
    print('profit : {}'.format(knapsack(info['weight'], info['value'], info['total_weight'], info['n'])))
