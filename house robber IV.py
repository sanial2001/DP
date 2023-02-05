class Solution:
    def solve(self, nums, index, option, cnt, k, val):
        if index == len(nums) or cnt == k:
            # print(cnt, val)
            if cnt == k:
                return val
            return float("inf")
        if (index, option, cnt, val) in self.d:
            return self.d[(index, option, cnt, val)]
        if option == "take":
            val = max(val, nums[index])
            self.d[(index, option, cnt, val)] = self.solve(nums, index + 1, "no_take", cnt + 1, k, val)
            return self.d[(index, option, cnt, val)]
        elif option == "no_take":
            b = self.solve(nums, index + 1, "take", cnt, k, val)
            c = self.solve(nums, index + 1, "no_take", cnt, k, val)
            self.d[(index, option, cnt, val)] = min(b, c)
            return self.d[(index, option, cnt, val)]

    def minCapability(self, nums: List[int], k: int) -> int:
        self.d = {}
        x = self.solve(nums, 0, "take", 0, k, float("-inf"))
        y = self.solve(nums, 0, "no_take", 0, k, float("-inf"))
        return min(x, y)
