"""
problem:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space

Sample Input 0
5
2 3 6 6 5
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    win = arr[0]
    #1. Find the winner manually
    for item in range(n):
        if arr[item] > win:
            win = arr[item]
            
        
    runnerup = None
    #2. find the runner manually
    for item in range(n):
        if win != arr[item]:
            if (runnerup is None) or (arr[item] > runnerup):
                runnerup = arr[item]
                
    print(runnerup) 


"""
Input:
5
2 3 6 6 5

Ouput: 
6
"""


#----------------------------------- two pointer solution failed at some cases --------------------------
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     first = 0
#     last = n-1

#     win = 0
#     runnerup = 0

#     while first <= last:
#         if arr[first] < arr[last]:
#             win = arr[last]
#             runnerup = arr[first]

#             first +=1

#         elif arr[first] >= arr[last]:
#             win = arr[first]
#             runnerup = arr[last]

#             last -=1

#         elif arr[first]  == arr[last]:
#             break
#     print(runnerup)