class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        inc, dec = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc = dec + 1
            elif nums[i] < nums[i-1]:
                dec = inc + 1
        return max(inc, dec)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    print(Solution().wiggleMaxLength(nums))
