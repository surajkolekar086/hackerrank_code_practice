"""
https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
"""

"""
Sample input:
9 27

Sample output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# Read input values
X, Y = map(int, input().split())

# Top half of the mat
for i in range(1, X, 2):
    pattern = (".|." * i).center(Y, "-")
    print(pattern)

# Center of the mat
print("WELCOME".center(Y, "-"))

# Bottom half of the mat
for i in range(X - 2, 0, -2):
    pattern = (".|." * i).center(Y, "-")
    print(pattern)
