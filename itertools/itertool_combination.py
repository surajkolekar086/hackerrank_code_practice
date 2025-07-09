#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

from itertools import combinations

# Input
s, k = input().split()
k = int(k)

# Sort the string to ensure lexicographic order
s = sorted(s)

# Generate and print combinations of length 1 to k
for i in range(1, k + 1):
    for comb in combinations(s, i):
        print(''.join(comb))


"""
Input:
    HACK 2
Output:

    A
    C
    H
    K
    AC
    AH
    AK
    CH
    CK
    HK

"""