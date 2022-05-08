class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        n = len(intervals)
        if n == 1:
            return 0
        intervals.sort()
        # print(intervals)
        t = [1 for _ in range(n)]

        for i in range(1, n):
            j = i - 1
            temp = []
            while j >= 0:
                if intervals[i][1] > intervals[j][1]:
                    temp.append(t[j])
                j = j - 1
            if len(temp) > 0:
                t[i] = max(temp) + 1

        return n - max(t)


if __name__ == '__main__':
    Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
