# In the first line,print True if has any alphanumeric characters.Otherwise, print False.
# In the second line, print True if has any alphabetical characters.Otherwise, print False.
# In the third line, print True if has any digits.Otherwise, print False.
# In the fourth line, print True if has any lowercase characters.Otherwise, print False.
# In the fifth line, print True if has any uppercase characters.Otherwise, print False.


if __name__ == '__main__':
    s = input()
    for x in range(len(s)):
        if s[x].isalnum():
            print(True)
            break
    else:
        print(False)

    for x in range(len(s)):
        if s[x].isalpha():
            print(True)
            break
    else:
        print(False)

    for x in range(len(s)):
        if s[x].isdigit():
            print(True)
            break
    else:
        print(False)

    for x in range(len(s)):
        if s[x].islower():
            print(True)
            break
    else:
        print(False)

    for x in range(len(s)):
        if s[x].isupper():
            print(True)
            break

    else:
        print(False)
