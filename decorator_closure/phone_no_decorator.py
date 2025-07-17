#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true

def wrapper(f):
    def fun(l):
        standard = []
        for num in l:
            n = num[-10:]
            standard.append(f"+91 {n[:5]} {n[5:]}")
        standard.sort()  # Sort the standardized numbers
        return f(standard)
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
"""
Sample input:
    3
    07895462130
    919875641230
    9195969878

Output:
    +91 78954 62130
    +91 91959 69878
    +91 98756 41230

"""



#Decorator simple example:
def outer(func):
    def inner():
        print("Timer started.........!!")
        func() #this is actual main() calling
        print("Timer stopped.......!!")
    
    return inner  #here we are not calling inner returning inner.

@outer  # outer(main)
def main():
    print("Actual code start")

main()