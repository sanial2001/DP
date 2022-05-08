def solve(n):
    if n == 1 or n == 2:
        return 1
    temp = []
    for i in range(1, n):
        temp.append(i * max(solve(n-i), n-i))
    return max(temp)


class Solution:
    def integerBreak(self, n: int) -> int:
        t = [-1 for _ in range(n+1)]
        t[0], t[1], t[2] = 0, 1, 1
        for i in range(3, n+1):
            temp = []
            for j in range(1, i):
                temp.append(j * max(t[i-j], i-j))
            t[i] = max(temp)
        return t[n]


if __name__ == '__main__':
    for i in range(3, 20):
        print(Solution().integerBreak(i))
