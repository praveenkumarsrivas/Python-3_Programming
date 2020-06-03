def minion_game(s):
    # for vowels
    l = len(s)
    c1 = 0
    c2 = 0
    for i in range(l):
        if s[i] in "AEIOU":
            for j in range(i, l+1):
                # print(s[i:j])
                if s[i:j] not in " ":
                    c1 += 1
    # print(c1)

    for i in range(l):
        if s[i] not in "AEIOU":
            for j in range(i, l + 1):

                if s[i:j] not in " ":
                    # print(s[i:j])
                    c2 += 1
    # print(c1)

    if c2 > c1:
        print("Stuart", c2)
    else:
        print("Kevin", c1)


minion_game(input())

