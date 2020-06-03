from collections import Counter
n = int(input())
shop = list(map(int, input().split()))
c_number = int(input())
counter_shop = Counter(shop)

sale = 0
while c_number > 0:
    size, cost = input().split()
    size = int(size)
    cost = int(cost)
    for x, y in counter_shop.items():
        if size == x and y >= 1:
            sale += cost
            counter_shop[x] = y-1
    #print(counter_shop)
    c_number -= 1

print(sale)


# 55 45 40 60
