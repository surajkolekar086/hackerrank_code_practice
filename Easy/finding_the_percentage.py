"""
Problem:
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for item, values in student_marks.items():
        if item == query_name:
            avg_marks = sum(student_marks[query_name])/ len(student_marks[query_name])
            #print(avg_marks) #Here it will print upto one decimal like --> 56.0 only but in problem statment we have to print upto 2 decimal 
            print(f"{avg_marks:.2f}") #Using this string format it will print upto 2 decimal --> 56.00

"""
Sample Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:
56.00
"""