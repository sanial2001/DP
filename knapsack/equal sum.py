def subsetsum(arr, S, N):
    #print(S, N)
    t = [[0 for j in range(S+1)] for i in range(N+1)]

    for i in range(N+1):
        t[i][0] = True
    for i in range(1, S+1):
        t[0][i] = False

    for n in range(1, N+1):
        for s in range(1, S+1):
            if arr[n-1] <= s:
                t[n][s] = t[n-1][s-arr[n-1]] or t[n-1][s]
            elif arr[n-1] > s:
                t[n][s] = t[n-1][s]

    return t[N][S]

def equalsum(arr, n):
    sum_of_elements = 0
    for ele in arr:
        sum_of_elements = sum_of_elements + ele
    if sum_of_elements % 2 != 0:
        return False
    else:
        return subsetsum(arr, sum_of_elements//2, n)


if __name__=='__main__':
    arr = [1, 5, 5, 11]
    n = 4
    if equalsum(arr, n):
        print('yes')
