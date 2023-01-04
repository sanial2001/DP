if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print("YES")
            val = 1
            res = []
            for i in range(n):
                val *= -1
                res.append(val)
            print(*res)
        else:
            print("NO")
