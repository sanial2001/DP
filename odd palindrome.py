class Solution:
    def solve(self, s):
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                return False
        return True
