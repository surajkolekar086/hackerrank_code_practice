"""
Problem: You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""
#-------------------- solution 1

# def swap_case(s):
#     new_str =""
#     for single_char in s:
#         if single_char.islower():
#             new_str += single_char.upper()
#         elif single_char.isupper():
#             new_str += single_char.lower()
#         else:
#             new_str += single_char

#     return new_str

#-------------------- solution 2 
# Swap cases without using built in funcitons
def swap_case(s):
    new_str =""
    for single_char in s:
        ascci = ord(single_char)  #Gets ASCII value
        if 65 <= ascci <= 90:
            new_str += chr(ascci + 32) # chr converts ASCII value back to character.
        elif 97 <= ascci <= 122:
            new_str += chr(ascci - 32)
        else:
            new_str += single_char
        #Difference between upper and lower letters in ASCII is 32:
    return new_str



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)