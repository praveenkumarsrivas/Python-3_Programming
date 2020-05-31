# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap


def wrap(string, max_width):
    string = (textwrap.wrap(string, max_width))
    s = ""
    for x in string:
        s += x + '\n'
    s = s[:len(s)-1]
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
