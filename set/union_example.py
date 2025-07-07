# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
    .union()

    The .union() operator returns the union of a set and the set of elements in an iterable.
    Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
    Set is immutable to the .union() operation (or | operation).

"""
"""
Task:
    Task

    The students of District College have subscriptions to English and French newspapers. 
    Some students have subscribed only to English, some have subscribed to only French and 
    some have subscribed to both newspapers.

    You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
    and the other set is subscribed to the French newspaper. The same student could be in both sets. 
    Your task is to find the total number of students who have subscribed to at least one newspaper.

"""

from itertools import count

english = int(input())
english_roll = set(map(int,input().split()))

french = int(input())
french_roll = set(map(int, input().split()))

s = english_roll.union(french_roll)
print(len(s))


"""
Input:
    9
    1 2 3 4 5 6 7 8 9
    9
    10 1 2 3 11 21 55 6 8

Output:
    13
"""