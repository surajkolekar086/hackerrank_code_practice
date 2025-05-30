

#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
"""
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

 print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
"""
"""
Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, 
she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Input: 
10     --> size of array                                
161 182 161 154 176 170 167 171 170 174

Output:
169.375 --> print upto 3 decimals only


"""



def average(array):
    # your code goes here
    avg_dist_height = set(array)
    
    
    avg_ar = sum(avg_dist_height) / len(avg_dist_height)
    
    total = round(avg_ar,3)
    return total
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)