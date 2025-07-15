"""
Exception:
    Error detected during execution are called exception

Example:
    ZeroDivisionError - 
        Error raised when the second argument of a division or module operation is zero.

    ValueError:
        The error is raised when a built-in operation of function recieves an argument that has the right type but an
        inappropriagte value.

    Handling Exceptions
        The statements try and except can be used to handle selected exceptions. 
        A try statement may have more than one except clause to specify handlers for different exceptions.

"""

n = int(input())

for _ in range(n):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as e:
        print("Error Code: ",e)

