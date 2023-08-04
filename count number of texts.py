class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        t = [0] * (n + 1)
        t[0] = 1

        for i in range(1, n + 1):
            t[i] = t[i - 1]
            if i - 2 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                t[i] += t[i - 2]
            if i - 3 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3]:
                t[i] += t[i - 3]
            if pressedKeys[i - 1] == '7' or pressedKeys[i - 1] == '9':
                if i - 4 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3] == pressedKeys[i - 4]:
                    t[i] += t[i - 4]

        return t[n] % (10 ** 9 + 7)
