import sys


def cut(n, x, y, z):
    if n == 0:
        return 0
    cut_x, cut_y, cut_z = 0, 0, 0
    if x < n:
        cut_x = 1 + cut(n - x, x, y, z)
    if y < n:
        cut_y = 1 + cut(n - y, x, y, z)
    if z < n:
        cut_z = 1 + cut(n - z, x, y, z)
    return max(cut_x, cut_y, cut_z)


def cut_dp(n, x, y, z):
    t = [-1 for _ in range(n+1)]
    t[0] = 0
    cut_x, cut_y, cut_z = -1000, -1000, -1000
    for i in range(1, n+1):
        if i >= x:
            cut_x = t[i-x]
        if i >= y:
            cut_y = t[i-y]
        if i >= z:
            cut_z = t[i-z]
        t[i] = 1 + max(cut_x, cut_y, cut_z)
    return t[n]


if __name__ == "__main__":
    print(cut_dp(7, 5, 2, 5))
