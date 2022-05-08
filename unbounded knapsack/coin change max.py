def coin_change(coin, s, n):
    if s == 0:
        return 1
    elif n == 0:
        return 0

    if coin[n-1] <= s:
        return coin_change(coin, s-coin[n-1], n) + coin_change(coin, s, n-1)
    elif coin[n-1] > s:
        return coin_change(coin, s, n-1)


def coin_change_dp(coin, S, N):
    t = [[-1 for y in range(S+1)] for x in range(N+1)]

    for n in range(N+1):
        t[n][0] = 1
    for s in range(1, S+1):
        t[0][s] = 0

    for n in range(1, N+1):
        for s in range(1, S+1):
            if coin[n-1] <= s:
                t[n][s] = t[n][s-coin[n-1]] + t[n-1][s]
            elif coin[n-1] > s:
                t[n][s] = t[n-1][s]

    return t[N][S]


if __name__ == '__main__':
    info = {
        'coin': [1, 2, 3],
        'sum': 4,
        'n': 3
    }
    print(coin_change_dp(info['coin'], info['sum'], info['n']))
