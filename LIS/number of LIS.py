class Solution:
    def findNumberOfLIS(self, nums) -> int:
        n = len(nums)
        t = [1 for _ in range(n)]
        c = [1 for _ in range(n)]

        for i in range(1, n):
            j = i-1
            temp = []
            while j >= 0:
                if nums[i] > nums[j]:
                    temp.append(t[j])
                j = j-1
            if len(temp) > 0:
                m = max(temp)
                t[i] = m + 1
                c[i] = t.count(m)
            else:
                m = max(t)
                c[i] = t.count(m)

        print(t, c)


if __name__ == '__main__':
    nums = [2,2,2,2,2]
    Solution().findNumberOfLIS(nums)
