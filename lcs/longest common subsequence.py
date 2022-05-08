def lcs(str1, str2, m, n):
    if m == 0 or n == 0:
        return 0

    if str1[m-1] == str2[n-1]:
        return 1 + lcs(str1, str2, m-1, n-1)
    else:
        return max(lcs(str1, str2, m, n-1),
                   lcs(str1, str2, m-1, n))


if __name__ == '__main__':
    info = {
        'str1': 'abcdgh',
        'str2': 'abedfhr',
        'm': 6,
        'n': 7
    }
    print(lcs(info['str1'], info['str2'],
              info['m'], info['n']))
