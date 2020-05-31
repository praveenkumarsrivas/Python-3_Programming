# Sample Input:
                # abracadabra
                # 5 k

# Sample Output:    
                # abrackdabra
# Using any of the methods explained above, replace the character at index k with giving character .


def mutate_string(string, position, character):
    new = ""
    new=string[:position]+character+string[position+1:]
    return new


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
