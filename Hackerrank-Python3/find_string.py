# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2


def count_substring(string, sub_string):
    l = len(string)
    c = 0
    match = ""
    indx = 0
    x = 0
    z = 0
    for x in range(l):
        z = 0
        z = x
        for y in range(len(sub_string)):
            match += string[z]
            z += 1
            if (z > (l - 1)):
                break
            #print(z)

        if (match == sub_string):
            c += 1
            z = 0
            match = ""
        else:
            match = ""
            z=0

    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
