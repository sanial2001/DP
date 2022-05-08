def rod_cutting(price, N):
    rod_length = N
    length = [(i + 1) for i in range(N)]
    t = [[-1 for y in range(rod_length + 1)] for x in range(N + 1)]

    for i in range(N + 1):
        for j in range(rod_length + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for n in range(1, N + 1):
        for w in range(1, rod_length + 1):
            if length[n - 1] <= w:
                t[n][w] = max(price[n - 1] + t[n][w - length[n - 1]], t[n - 1][w])
            elif length[n - 1] > w:
                t[n][w] = t[n - 1][w]

    return t[N][rod_length]


if __name__ == '__main__':
    info = {
        'price': [3, 5, 8, 9, 10, 17, 17, 20],
        'n': 8
    }
    print('profit : {}'.format(rod_cutting(info['price'], info['n'])))
