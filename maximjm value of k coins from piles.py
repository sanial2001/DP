class Solution:
    def solve(self, piles, index, k):
        if index >= len(piles) or k == 0:
            return 0
        discard = self.solve(piles, index + 1, k)
        accept = 0
        for i in range(1, k + 1):
            if i - 1 < len(piles[index]):
                accept = max(accept, self.solve(piles, index + 1, k - i) + piles[index][i - 1])
        return max(discard, accept)

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for i, pile in enumerate(piles):
            for j in range(1, len(pile)):
                pile[j] += pile[j - 1]

        return self.solve(piles, 0, k)


class SolutionMemo:
    def solve(self, piles, index, k):
        if index >= len(piles) or k == 0:
            return 0
        if (index, k) in self.d:
            return self.d[(index, k)]
        discard = self.solve(piles, index + 1, k)
        accept = 0
        for i in range(1, min(len(piles[index]) + 1, k + 1)):
            accept = max(accept, self.solve(piles, index + 1, k - i) + piles[index][i - 1])
        self.d[(index, k)] = max(discard, accept)
        return self.d[(index, k)]

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for i, pile in enumerate(piles):
            for j in range(1, len(pile)):
                pile[j] += pile[j - 1]
        self.d = {}
        return self.solve(piles, 0, k)