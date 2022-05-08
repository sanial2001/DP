def getCount(N):
    # code here
    t = [1 for i in range(10)]
    phone = []

    for i in range(1, N):
        phone = t.copy()
        print(phone)
        t[0] = phone[0] + phone[8]
        t[1] = phone[1] + phone[2] + phone[4]
        t[2] = phone[2] + phone[1] + phone[3] + phone[5]
        t[3] = phone[3] + phone[2] + phone[6]
        t[4] = phone[4] + phone[1] + phone[5] + phone[7]
        t[5] = phone[5] + phone[2] + phone[4] + phone[6] + phone[8]
        t[6] = phone[6] + phone[3] + phone[5] + phone[9]
        t[7] = phone[7] + phone[4] + phone[8]
        t[8] = phone[8] + phone[5] + phone[9] + phone[7] + phone[0]
        t[9] = phone[9] + phone[8] + phone[6]

    print(sum(t))


if __name__ == '__main__':
    getCount(3)