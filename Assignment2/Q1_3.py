import math
arr = [1,4,6,10,18,3,5,2,40,20,25,11,15,12,65,23,8]

def isMax(arr, v, max):
    if arr[v] > max:
        max = arr[v]
        if len(arr)-1 == v:
            print(max)
            return
        isMax(arr, v+1, max)
    else:
        if len(arr)-1 == v:
            print(max)
            return
        isMax(arr, v +1, max)
isMax(arr, 0, 0)

def findSum(arr, v, sum):
    if len(arr) == v:
        print(sum)
    else:
        sum =  sum + arr[v]
        findSum(arr, v+1, sum)
findSum(arr, 0, 0)

def partition(arr):
    if len(arr) == 1:
        return 0
    i = -1
    n = len(arr)-1
    pivot = arr[n]
    for j in range(0 , n):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[n] = arr[n],arr[i+1]
    return ( i+1 )
print(partition(arr))

'''
def f(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y
'''

