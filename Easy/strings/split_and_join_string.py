"""
problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

input: this is a string
ouput: this-is-a-string
"""

def split_and_join(line):
    # write your code here
    a = line.split(" ")
    return "-".join(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

    """
Method	Purpose	Input Type	Output Type
    split()	Split string → list	str	list
    join()	Join list → string (with separator)	iterable of str	str
    
    """