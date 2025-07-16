n, x = map(int, input().split())

sub_marks = []
for _ in range(x):
    sub_marks.append(list(map(float, input().split())))

# Transpose to group marks by student
for student_marks in zip(*sub_marks):
    avg_marks = sum(student_marks) / x
    print(f"{avg_marks:.1f}")