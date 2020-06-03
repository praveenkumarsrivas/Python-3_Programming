def minion_game(s):
    st = 0
    ke = 0
    v = 'AEIOU'
    c = 0
    x = 0
    y = 0
    chk = ""
    life = 0
    ss = set(list(s))
    ss = list(ss)
    ss = ",".join(ss)
    vv = 0
    for t in range(len(s)):
        if v.count(s[t]) == 1:
            vv += 1

    total_v = ss.count('A')+ss.count('E')+ss.count('I') + \
        ss.count('O') + ss.count('U')

    for i in range(len(s)):
        c = v.count(s[i])
        if c == 1:
            life += 1
            for j in range(i, len(s)):
                chk = s[i:j+i]
                for k in range(len(s)):
                    if chk == s[k: len(chk) + k]:
                        x += 1
                print(chk, x)
                ke += x
                x = 0
            if life == total_v:
                break
    life = 0

    for i in range(len(s)):
        if s[i] not in v:
            life += 1
            for j in range(i, len(s)):
                chk = s[i: j+1]
                # print(chk)
                for k in range(len(s)):
                    if chk == s[k: len(chk) + k]:
                        y += 1
                print(chk, y)
                st += y
                y = 0
            if life == abs(total_v - vv):
                break

    # if st > ke:
    #     print("Stuart", st)
    # else:
    #     print("Kevin", ke)


if __name__ == '__main__':
    s = input()
    minion_game(s)


# Sample Input

# BANANA
# Sample Output

# Stuart 12
