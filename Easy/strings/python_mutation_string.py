"""
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

Sample Input:
    abracadabra     s = 'abracadabra'
    5 k             position = 5, character = 'k'

Ouput:
    abrackdabra
"""


def mutate_string(string, position, character):
    #approach 1
    #Convert the string to a list and then change the value.
    l = list(string)
    l[position] = character
    string = ''.join(l)
    
    #approach 2
    #slice the string and join it back
    #string = string[:5] + 'K' + string[6:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)