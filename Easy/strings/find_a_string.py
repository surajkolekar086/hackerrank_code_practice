"""
Given a string and a substring, count how many times the substring appears in the string.
Substring matches can overlap. Traverse left to right only.
"""
#ABCDCDC 7
#CDC    2
 
def count_substring(string, sub_string):
    count = 0
    print(len(string))
    le = len(string) - len(sub_string)
    print(le)
    for i in range(le + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

# Test case
string = "ABCDCDC"
sub_string = "CDC"
string = input().strip()
sub_string = input().strip()

print("Occurrences:", count_substring(string, sub_string))
