class Solution:
    def solve(self, dice, n, d, target, t):
        if d == 0 or target < 0:
            if target == 0:
                return 1
            return 0
        if t[d][target] == -1:
            x = 0
            for i in range(n):
                x += self.solve(dice, n, d-1, target-dice[i], t)
            t[d][target] = x % (1000000007)
            return t[d][target]
        else:
            return t[d][target]

    def solve_dp(self, d, f, target):
        t = [[0 for _ in range(target+1)] for _ in range(d+1)]
        t[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, target+1):
                temp = 0
                for k in range(1, f+1):
                    if j-k >= 0:
                        temp += t[i-1][j-k]
                t[i][j] = temp % (10**9 + 7)
        for val in t:
            print(val)
        return t[d][target]

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        arr = [i+1 for i in range(f)]
        t = [[-1 for _ in range(1001)] for _ in range(1001)]
        #print(self.solve(arr, len(arr), d, target, t))
        print(self.solve_dp(d, f, target))


if __name__ == '__main__':
    Solution().numRollsToTarget(d = 2, f = 6, target = 7)
