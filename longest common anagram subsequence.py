class Solution:
    def solve(self, a, b):
        f1, f2 = [0] * 26, [0] * 26

        for i in range(len(a)):
            f1[ord(a[i]) - ord('a')] += 1
        for i in range(len(b)):
            f2[ord(b[i]) - ord('a')] += 1

        ans = 0
        for i in range(26):
            ans += min(f1[i], f2[i])
        return ans
