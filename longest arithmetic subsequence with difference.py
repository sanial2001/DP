class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = collections.defaultdict(int)
        t = [1 for _ in range(len(arr))]

        # res = 0
        for i, num in enumerate(arr):
            if num - difference in d:
                t[i] = t[d[num - difference]] + 1
            d[num] = i
        # print(t)

        return max(t)
