import collections


def solve(frm, to, inp):
    mn_len = min(len(frm), len(to))
    res = ''
    frm = list(frm[:mn_len])  # converting string to list for ease of use in map
    to = list(to[:mn_len])
    mp = {}
    for i, val in enumerate(frm):  # this is map creation
        mp[val] = to[i]

    for i in inp:
        if i in mp:
            res += mp[i]
        else:
            res += i

    return res


if __name__ == "__main__":
    print(solve('ABCD', 'efgh', 'AGREED'))
