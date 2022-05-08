class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        t1, t2 = [values[0]], [values[0]]
        for i in range(1, n):
            t1.append(max(values[i] + i, t1[i - 1]))
            t2.append(values[i] - i)
        t1, t2 = t1[:-1], t2[1:]
        # print(t1, t2)
        ans = 0
        for i in range(n - 1):
            ans = max(ans, t1[i] + t2[i])
        return ans
