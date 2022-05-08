class Solution:
    def dfs(self, s, i):
        if i < 0 or i >= len(s) or s[i] != '0':
            return
        if i == len(s) - 1:
            self.ans = True
            return
        for jump in range(self.low, self.high + 1):
            self.dfs(s, i + jump)

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        self.low = minJump
        self.high = maxJump
        self.ans = False
        self.dfs(s, 0)
        return self.ans


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = [0]
        far = 0
        while q:
            ind = q.pop(0)
            if ind == len(s) - 1:
                return True
            low = max(far + 1, ind + minJump)
            high = min(len(s) - 1, ind + maxJump)
            for jump in range(low, high + 1):
                if s[jump] == '0':
                    q.append(jump)
            far = ind + maxJump
        return False


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = [0]
        far = 0
        while q:
            ind = q.pop(0)
            low = max(far + 1, ind + minJump)
            high = min(len(s) - 1, ind + maxJump)
            for jump in range(low, high + 1):
                if s[jump] == '0':
                    q.append(jump)
                    if jump == len(s) - 1:
                        return True
            far = ind + maxJump
        return False
