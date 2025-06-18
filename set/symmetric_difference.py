

"""
Concept:
    .split() — by default, splits the string by spaces and returns a list of strings.
    Example:
    a = input() #1 2 3 4
    lis = a.split()
    print(lis) #['1', '2', '3', '4']

set():
    - Unordered items
    - add() 
    - update()
    - discard() -> if item not in the set, wont give any error.
    - remove()  -> apposite of discard() method.

    - union => a.union(b) --> all values which are exist in a or b (no duplicates)
    - intersection => a.intersection(b) --> common values in a or b
    - difference => a.difference(b)     --> Values which exist in a but not in b

"""

"""
Task:
    Given 2 sets of integers, n and m, print their symmetric difference in ascending order. 
    The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

    Input:
    4           set a size M = 4
    2 4 5 9     a = {2, 4, 5, 9}
    4           set b size N = 4
    2 4 11 12   b = {2, 4, 11, 12}

    Output:
    5
    9
    11
    12
"""


n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

result = sorted( a ^ b)

for item in result:
    print(item)