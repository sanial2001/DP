def wordBreak(line, dictionary):
    # Complete this function
    n = len(line)
    t = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            word = line[j:i + 1]
            if word in dictionary:
                if j > 0:
                    t[i] = t[i] + t[j-1]
                else:
                    t[i] = t[i] + 1

    print(t)


if __name__ == '__main__':
    d = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
    a = 'ilike'
    wordBreak(a, d)
