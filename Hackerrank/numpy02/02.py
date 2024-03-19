import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a=(numpy.array(arr, float))
    reversed_arr = a[::-1]
    return reversed_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)