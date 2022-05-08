t = [[-1 for x in range(100)] for y in range(1000)]


def knapsack(w, val, wt, n):
    if n == 0 or wt == 0:
        return 0

    if t[n][wt] == -1:
        if val[n - 1] <= wt:
            t[n][wt] = max(val[n - 1] + knapsack(w, val, wt - w[n - 1], n - 1), knapsack(w, val, wt, n - 1))
            return t[n][wt]
        elif val[n - 1] > wt:
            t[n][wt] = knapsack(w, val, wt, n - 1)
            return t[n][wt]
    else:
        return t[n][wt]


if __name__ == '__main__':
    info = {
        'weight': [1, 3, 4, 5],
        'value': [1, 4, 5, 7],
        'total_weight': 7,
        'n': 4
    }
    print('profit : {}'.format(knapsack(info['weight'], info['value'], info['total_weight'], info['n'])))
