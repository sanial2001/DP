class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i, val in enumerate(arr):
            d[val].append(i)

        visited = [False for _ in range(n)]
        q = [0]
        visited[0] = True
        ans = 0
        while q:
            for i in range(len(q)):
                ind = q.pop(0)
                # print(ind)
                if ind == n - 1:
                    return ans
                if ind + 1 < n and visited[ind + 1] == False:
                    visited[ind + 1] = True
                    q.append(ind + 1)
                if ind - 1 > 0 and visited[ind - 1] == False:
                    visited[ind - 1] = True
                    q.append(ind - 1)
                for nei in d[arr[ind]]:
                    if visited[nei] == False:
                        visited[nei] = True
                        q.append(nei)
                del d[arr[ind]]
            ans += 1
