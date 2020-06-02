n = int(input())
l = list()
for i in range(n):
    x = input()
    if x.count(" ") == 2:
        command, pos, element = x.split(" ")
        if (command == "insert"):
            # print("inserting..")
            pos = int(pos)
            element = int(element)
            l.insert(pos, element)
            # print(l)

    if x.count(" ") == 1:
        command, element = x.split(" ")
        element = int(element)
        if (command == "remove"):
            l.remove(element)
            # print("removed")
        elif (command == "append"):
            l.append(element)

    else:
        command = x
        if (command == "print"):
            # print("printing..")
            print(l)
        elif (command == "sort"):
            l.sort()
        elif (command == "pop"):
            l.pop()
        elif (command == "reverse"):
            l.reverse()


# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
