if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i,j,k] for i in range(x+1)
                      for j in range(y+1)
                      for k in range(z+1) if (i+j+k) != n]
                      
    print(result)

    """
    input: 1 1 2 3
    ouput: [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
    """