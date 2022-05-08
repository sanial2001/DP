def longest_common_substring(x, y, M, N):
    t = [[-1 for y in range(N+1)] for x in range(M+1)]

    for i in range(M+1):
        for j in range(N+1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for m in range(1, M+1):
        for n in range(1, N+1):
            if x[m-1] == y[n-1]:
                t[m][n] = 1 + t[m-1][n-1]
            else:
                t[m][n] = 0

    max_ele = max(max(i) for i in t)
    return max_ele


if __name__ == '__main__':
    info = {
        'str1': 'abcdgh',
        'str2': 'abedfhr',
        'm': 6,
        'n': 7
    }
    print(longest_common_substring(info['str1'], info['str2'],
                                   info['m'], info['n']))
