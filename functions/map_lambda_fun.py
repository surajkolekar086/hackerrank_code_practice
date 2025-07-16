cube = lambda x: x ** 3  # complete the lambda function 

def fibonacci(n):
    fin_sq = []
    a,b = 0,1
    for _ in range(n):
        fin_sq.append(a)
        a, b = b, a + b
    return fin_sq

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


"""
5
[0, 1, 1, 8, 27]

"""