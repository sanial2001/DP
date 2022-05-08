import sys


def coin_change_min_coins(coin, S, N):
    t = [[-1 for y in range(S+1)] for x in range(N+1)]

    for i in range(S+1):
        t[0][i] = sys.maxsize - 1
    for i in range(1, N+1):
        t[i][0] = 0
    for i in range(1, S+1):
        if i % coin[0] == 0:
            t[1][i] = i//coin[0]
        else:
            t[1][i] = sys.maxsize - 1

    for n in range(2, N+1):
        for s in range(1, S+1):
            if coin[n-1] <= s:
                t[n][s] = min(1 + t[n][s-coin[n-1]], t[n-1][s])
            elif coin[n-1] > s:
                t[n][s] = t[n-1][s]
    if t[N][S] == sys.maxsize-1:
        return -1
    else:
        return t[N][S]


if __name__ == '__main__':
    info = {
        'coin': [4, 3],
        'sum': 2,
        'n': 2
    }
    print(coin_change_min_coins(info['coin'], info['sum'], info['n']))
