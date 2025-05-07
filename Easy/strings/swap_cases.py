"""
Problem: You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""

def swap_case(s):
    new_str =""
    for single_char in s:
        if single_char.islower():
            new_str += single_char.upper()
        elif single_char.isupper():
            new_str += single_char.lower()
        else:
            new_str += single_char

    return new_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)