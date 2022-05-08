def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    t = [[0 for _ in range(n)] for _ in range(n)]

    for g in range(n):
        i = 0
        for j in range(g, n):
            if g == 0:
                t[i][j] = 1
            elif g == 1:
                if s[i] == s[j]:
                    t[i][j] = 1
                else:
                    t[i][j] = 0
            else:
                if s[i] == s[j] and t[i + 1][j - 1] == 1:
                    t[i][j] = 1
                else:
                    t[i][j] = 0
            i = i + 1

    for val in t:
        print(val)

    sum_ele = 0
    for val in t:
        sum_ele += sum(val)

    return sum_ele


if __name__ == '__main__':
    str = 'abccbc'
    print(countSubstrings(str))
