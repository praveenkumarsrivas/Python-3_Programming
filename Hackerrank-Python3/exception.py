# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    try:
        a, b = input().split(" ")
        a = int(a)
        b = int(b)
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
