"""
Sample input:
    5

sample output:

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------


"""
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        # Take letters from current to 'a', then reverse
        s = alpha[size-1:i:-1] + alpha[i:size]
        line = '-'.join(s)
        # Center the line with '-'
        lines.append(line.center(4*size - 3, '-'))

    # Mirror top and bottom
    full_rangoli = lines[::-1] + lines[1:]
    
    for line in full_rangoli:
        print(line)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)