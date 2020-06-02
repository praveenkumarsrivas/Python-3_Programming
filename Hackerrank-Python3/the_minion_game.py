def minion_game(s):
    st = 0
    ke = 0
    v = 'aeiou'
    c = 0
    for i in range(len(s)):
        c = v.count(s[i])
        if c == 1:
            for j in range(i, len(s)):
                print(s[i:j])


if __name__ == '__main__':
    s = input()
    minion_game(s)


# Sample Input

# BANANA
# Sample Output

# Stuart 12
