class Solution:
    def dfs(self, arr, i, visited):
        if i < 0 or i >= len(arr) or visited[i] == True:
            return
        if arr[i] == 0:
            self.ans = True
            return
        visited[i] = True
        self.dfs(arr, i + arr[i], visited)
        self.dfs(arr, i - arr[i], visited)
        visited[i] = False

    def canReach(self, arr: List[int], start: int) -> bool:
        self.ans = False
        n = len(arr)
        visited = [False for _ in range(n)]
        self.dfs(arr, start, visited)
        return self.ans
