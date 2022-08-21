class Solution:
    def solve(self, jobs, i, prev):
        n = len(jobs)
        if i == n:
            return 0
        if jobs[i][0] >= prev:
            return max(self.solve(jobs, i + 1, jobs[i][1]) + jobs[i][2], self.solve(jobs, i + 1, prev))
        else:
            return self.solve(jobs, i + 1, prev)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)))
        return self.solve(jobs, 0, float("-inf"))


class Solution_memo:
    def solve(self, jobs, i, prev):
        n = len(jobs)
        if i == n:
            return 0
        if (i, prev) in self.d:
            return self.d[(i, prev)]
        if jobs[i][0] >= prev:
            self.d[(i, prev)] = max(self.solve(jobs, i + 1, jobs[i][1]) + jobs[i][2], self.solve(jobs, i + 1, prev))
            return self.d[(i, prev)]
        else:
            self.d[(i, prev)] = self.solve(jobs, i + 1, prev)
            return self.d[(i, prev)]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.d = {}
        jobs = sorted(list(zip(startTime, endTime, profit)))
        return self.solve(jobs, 0, float("-inf"))


class Solution_heap:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)))
        pq = []
        total = 0

        for s, e, p in jobs:
            while pq and pq[0][0] <= s:
                end, pro = heapq.heappop(pq)
                total = max(total, pro)
            heapq.heappush(pq, (e, p + total))

        while pq:
            end, pro = heapq.heappop(pq)
            total = max(total, pro)

        return total
