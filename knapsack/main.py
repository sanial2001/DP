t = [[0 for x in range(11+1)] for y in range(5+1)]
arr = [2, 3, 7, 8, 10]

for n in range(5+1):
    for s in range(11+1):
        if s == 0:
            t[n][s] = True
        elif n == 0:
            t[n][s] = False
        if arr[n - 1] <= s:
            t[n][s] = t[n - 1][s - arr[n - 1]] or t[n - 1][s]
        elif arr[n - 1] > s:
            t[n][s] = t[n - 1][s]

for val in t:
    print(val)