class Solution:
    def solve(self, questions, index):
        if index >= len(questions):
            return 0
        if index in self.d:
            return self.d[index]
        buy = self.solve(questions, index + 1 + questions[index][1]) + questions[index][0]
        skip = self.solve(questions, index + 1)
        self.d[index] = max(buy, skip)
        return self.d[index]

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.d = {}
        return self.solve(questions, 0)
