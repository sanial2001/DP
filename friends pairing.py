def solve(n):
    if n <= 1:
        return 1
    return solve(n-1) + (n-1)*solve(n-2)


def solve_dp(n):
    t = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        t[i] = t[i-1] + (i-1)*t[i-2]
    return t[n]


if __name__  == '__main__':
    print(solve_dp(4))
