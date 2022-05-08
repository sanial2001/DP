class Solution:
    def minDays(self, n: int) -> int:
        ans = 0
        q = [n]
        visit = set()
        visit.add(n)
        while q:
            for i in range(len(q)):
                num = q.pop(0)
                if num == 0:
                    return ans
                if num and (num - 1) not in visit:
                    visit.add(num - 1)
                    q.append(num - 1)
                if num % 2 == 0 and num - (num // 2) not in visit:
                    visit.add(num - (num // 2))
                    q.append(num - (num // 2))
                if num % 3 == 0 and num - 2 * (num // 3) not in visit:
                    visit.add(num - 2 * (num // 3))
                    q.append(num - 2 * (num // 3))
            ans += 1
