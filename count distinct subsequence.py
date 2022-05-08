def solve(str):
    n = len(str)
    t = [-1 for _ in range(n + 1)]
    t[0] = 1

    for i in range(1, n + 1):
        j = i - 1
        k = j - 1
        temp = 0
        while k >= 0:
            if str[k] == str[j]:
                temp = t[k]
                break
            k = k - 1
        t[i] = (t[i - 1] * 2) - temp

    for val in t:
        print(val)

    return t[n]-1


if __name__ == '__main__':
    print(solve('aaa'))
