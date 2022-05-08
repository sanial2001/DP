class Solution:
    def lis(self, nums):
        n = len(nums)
        t = [1 for _ in range(n)]

        for i in range(1, n):
            j = i-1
            temp = []
            while j >= 0:
                if nums[i] > nums[j]:
                    temp.append(t[j])
                j = j-1
            if len(temp) > 0:
                t[i] = max(temp) + 1

        return t

    def minimumMountainRemovals(self, nums) -> int:
        lis = self.lis(nums)
        lds = self.lis(nums[::-1])[::-1]
        n = len(nums)
        t = [10000 for _ in range(n)]
        for i in range(n):
            if lis[i] == 1 or lds[i] == 1:
                continue
            else:
                t[i] = n - (lis[i] + lds[i] - 1)
        print(min(t))


if __name__ == '__main__':
    nums = [1,2,3,4,4,3,2,1]
    Solution().minimumMountainRemovals(nums)
