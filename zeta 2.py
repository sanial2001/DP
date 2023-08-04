class Solution:
    def maxDivScore(self, nums, divisors) -> int:
        res, mx = 0, 0
        seen = set()
        divisors.sort(reverse=True)
        for div in divisors:
            cnt = 0
            for num in nums:
                if num % div == 0:
                    cnt += 1
            print(div, cnt)
            if cnt in seen:
                res = div
            elif cnt > mx:
                seen.add(cnt)
                mx = cnt
                res = cnt
        return res if res != 0 else divisors[-1]


if __name__ == "__main__":
    print(Solution().maxDivScore(
        nums=[56, 22, 79, 41, 8, 39, 81, 59, 74, 14, 45, 49, 15, 10, 28, 16, 77, 22, 65, 8, 36, 79, 94, 44, 80, 72, 8,
              96, 78]
        ,
        divisors=[39, 92, 69, 55, 9, 44, 26, 76, 40, 77, 16, 69, 40, 64, 12, 48, 66, 7, 59, 10, 33, 72, 97, 60, 79, 68,
                  25, 63]))
