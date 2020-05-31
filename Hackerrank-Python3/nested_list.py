if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
    s = sorted(d.items(), key=lambda x: x[1], reverse=False)
    t = s[0][1]
    # print(t)
    for x in s:
        if x[1] > t:
            t = x[1]
            break
    newdic = {}
    for x in s:
        if (t == x[1]):
            newdic[x[0]] = x[1]
            #print(x[0], x[1])
    ls = sorted(newdic.keys())
    for x in ls:
        print(x)

'''
it's a mind boggling :) )p
'''
