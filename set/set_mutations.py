# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
"""

"""
Input:
     16
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
    4
    intersection_update 10
    2 3 5 6 8 9 1 4 7 11
    update 2
    55 66
    symmetric_difference_update 5
    22 7 35 62 58
    difference_update 7
    11 22 35 55 58 62 66
    
Output:
    38
    
"""


n = int(input())
n_set = set(map(int, input().split()))

num_operation = int(input())

for item in range(num_operation):
    operation = input().split()[0]
    op_set = set(map(int, input().split()))
    
    if operation == "intersection_update":
        n_set.intersection_update(op_set)
        
    elif operation == "update":
        n_set.update(op_set)
        
    elif operation == "symmetric_difference_update":
        n_set.symmetric_difference_update(op_set)
        
    elif operation == "difference_update":
        n_set.difference_update(op_set)
        
print(sum(n_set))