# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.

"""

n = int(input())
    
res = set()
for _ in range(n):
    stamp = input()
    res.add(stamp)
    
    
print(len(res))

"""
Input:
    7
    UK
    China
    USA
    France
    New Zealand
    UK
    France


Sample output:
    5
"""