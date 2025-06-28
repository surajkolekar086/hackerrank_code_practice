"""
Concept:
    .remove(x)
        This operation removes element x from the set.
        If element x does not exist, it raises a KeyError.
        The .remove(x) operation returns None.

    .discard(x)
        This operation also removes element x from the set.
        If element x does not exist, it does not raise a KeyError.
        The .discard(x) operation returns None.

    .pop()
        This operation removes and return an arbitrary element from the set.
        If there are no elements to remove, it raises a KeyError.

"""


"""
Task

    You have a non-empty set , and you have to execute  commands given in  lines.

    The commands will be pop, remove and discard.

    Input Format

    The first line contains integer , the number of elements in the set .
    The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
    The third line contains integer , the number of commands.
    The next  lines contains either pop, remove and/or discard commands followed by their associated value.

"""


n = int(input())
s = set(map(int, input().split()))

num = int(input())


for _ in range(num):
    command = input().strip().split()
    
    if command[0] =="pop":
        s.pop()
    elif command[0] =="remove":
        s.remove(int(command[1]))
    elif command[0]== "discard":
        s.discard(int(command[1]))
        
        
print(sum(s))