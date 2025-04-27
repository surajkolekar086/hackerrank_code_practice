
"""
problem:
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
    Berry
    Harry

"""

#------------------------------------------------------------ My approach
#
#Error: float is not ietable
""" gpt
float(input()) gives a single number, not a list.

You cannot make a list from a single float directly like that.

And also you are trying to loop over a single score, which is wrong.

Your thinking is close but you missed that you need to store BOTH name and score together (as a pair)
"""

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = list(float(input()))
        
#         #step1 find max score
#         max_score = score[0]
        
#         for marks in range(score):
#             if max_score < score[marks]:
#                 max_score = score[marks]
                
#         #2. find second max score
#         sec_max_score = []
        
#         for sec_max_score in range(score):
#             if (max_score != score[sec_max_score]) or (sec_max_score is None):
#                 sec_max_score.append(score[sec_max_score])
                
#         n = len(sec_max_score)
        
#         for i in range(n):
#             for j in range(0, n-i-1):
#                 if sec_max_score[j] > sec_max_score[j+1]:
#                     sec_max_score[j], sec_max_score[j+1] = sec_max_score[j+1], sec_max_score[j]
                    
#         for name in sec_max_score:
#             print(name)
            

#----------------------------------------------------------- working solution:

if __name__ == '__main__':
    students = []  # to store [name, score] pairs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    print(f"All students with name and scores {students=}") #students=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    # Step 1: Find the lowest score
    min_score = students[0][1]
    for student in students:
        if student[1] < min_score:
            print(f"student1 {student[1]}") #37.2
            min_score = student[1]

    # Step 2: Find second lowest score
    second_min = None
    for student in students:
        if student[1] != min_score:
            if (second_min is None) or (student[1] < second_min):
                second_min = student[1]

    # Step 3: Collect names with second lowest score
    names = []
    for student in students:
        if student[1] == second_min:
            names.append(student[0])

    # Step 4: Sort names alphabetically manually
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]

    # Step 5: Print each name on new line
    for name in names:
        print(name) 

    #Berry Harry