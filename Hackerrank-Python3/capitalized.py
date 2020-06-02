def solve(s):
    newS = list()
    newS = s.split(" ")
    # for x in newS:
    #     print (x)
    print(newS)
    newstr = " "
    ll = []
    for i in range(len(newS)):
        newS[i] = newS[i].capitalize()
    newstr = " ".join(newS)

    return newstr


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

# Sample Input:
# chrisalan

# Sample Output:
# Chris Alan
