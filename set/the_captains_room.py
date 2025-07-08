# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
task:
    https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

"""
"""
Input:
    5
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

Output:
    8

"""
from collections import Counter

size_of_group = int(input())

room_numbers = list(map(int, input().split()))

captain_room = 0

counts = Counter(room_numbers)

for room, count in counts.items():
    if count == 1:
        print(room)
        break
