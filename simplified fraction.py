class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        i = 1
        res, seen = [], set()
        while i < n:
            for j in range(i + 1, n + 1):
                if i != j and i / j not in seen:
                    res.append(str(i) + "/" + str(j))
                    seen.add(i / j)
            i += 1
        return res
