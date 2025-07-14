#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())  # number of students
columns = input().split()  # column names

# Get the index of the MARKS column
marks_index = columns.index("MARKS")

total_marks = 0
for _ in range(n):
    data = input().split()
    total_marks += int(data[marks_index])

average = total_marks / n
print(f"{average:.2f}")

"""
Input:
    5
    ID         MARKS      NAME       CLASS     
    1          97         Raymond    7
    2          50         Steven     4
    3          91         Adrian     9
    4          72         Stewart    5
    5          80         Peter      6   

Output:
    78.00


"""