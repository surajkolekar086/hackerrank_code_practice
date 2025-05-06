if __name__ == '__main__':
    N = int(input())
    new_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            new_list.insert(int(command[1]), int(command[2]))

        elif command[0] == "print":
            print(new_list)

        elif command[0] == "remove":
            new_list.remove(int(command[1]))

        elif command[0] == "append":
            new_list.append(int(command[1]))

        elif command[0] == "sort":
            new_list.sort()

        elif command[0] == "pop":
            new_list.pop()

        elif command[0] == "reverse":
            new_list.reverse()



  
"""
INPUT:

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
    
"""

"""
OUPUT:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""    