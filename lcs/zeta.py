class Solution:
    def solve(self, s):
        s2 = 2 * s
        max_len = 0
        for x in range(len(s)):
            for y in range(len(s) + 1):
                temp = s2[x: x + y]
                if temp == temp[::-1] and len(temp) > max_len:
                    max_len = len(temp)
        return max_len


ob = Solution()
s = "carzrace"
print(ob.solve(s))
