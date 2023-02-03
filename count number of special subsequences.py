class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        t, mod = [0] * 3, 10 ** 9 + 7

        for num in nums:
            if num == 0:
                t[0] = t[0] * 2 + 1
            elif num == 1:
                t[1] = t[1] * 2 + t[0]
            else:
                t[2] = t[2] * 2 + t[1]

        return t[2] % mod
