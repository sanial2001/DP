class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        t = [0 for _ in range(target + 1)]
        t[0] = 1
        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    t[i] += t[i - n]
        return t[target]
