#https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true


import operator

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return map(f, people) 
        # complete the function
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

"""
Sample Input:
    3
    Mike Thomson 20 M
    Robert Bustle 32 M
    Andria Bustle 30 F

Sample output:
    Mr. Mike Thomson
    Ms. Andria Bustle
    Mr. Robert Bustle
"""