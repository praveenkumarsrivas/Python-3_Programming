#Task
#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen

def split_and_join(line):
    s = ""
    s = line.split(" ")
    s = '-'.join(s)
    print(s)
split_and_join("praveen kumar srivas")
