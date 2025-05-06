
"""

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format
hast(t)


Sample Input:
2
1 2

Sample Ouput:
3713081631934410656

"""

n = int(input())
integer_list = tuple(map(int, input().split()))
print(integer_list)
print(hash(integer_list))