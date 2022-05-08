class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max, r_max = [0 for _ in range(n)], [0 for _ in range(n)]
        l_max[0], r_max[n - 1] = height[0], height[n - 1]

        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], height[i])

        max_ht = [0 for _ in range(n)]
        for i in range(n):
            max_ht[i] = min(l_max[i], r_max[i])

        ans = 0
        for i in range(n):
            ans += (max_ht[i] - height[i])

        return ans
