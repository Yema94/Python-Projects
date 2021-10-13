# Numerical Python

import numpy as np
print(np.__version__)

data = [1, 2, 3, 4, 5]
'''arr = np.array(data[0]) #0D Array
print(arr, "--", arr.ndim)

arr = np.array(data, ndmin=1, dtype='S') #1D Array
print(arr, "--", arr.ndim, "--",arr[-1], "--", type(arr), "--", arr.dtype)

arr = np.array(data, ndmin=2, dtype='U') #2D Array
print(arr, "--", arr.ndim, "--",arr[0,-1], "--", type(arr), "--", arr.dtype)

arr = np.array(data, ndmin=3, dtype='i') #3D Array
print(arr, "--", arr.ndim, "--",arr[0,0,-1], "--", type(arr), "--", arr.dtype)

arr = np.array(data, ndmin=4, dtype='c') #4D Array
print(arr, "--", arr.ndim, "--",arr[0,0,0,-1], "--", type(arr), "--", arr.dtype)'''


'''Coping the array and changing the data type'''
'''newarr = arr.astype(int) #and changing the data type to int
newarr = arr.astype('i') #another way to change the data type
newarr = arr.astype(bool) #changing the type to boolean'''


'''joinig arrays using concacenate and stack funtions'''
'''arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

print("stack")
arr = np.stack((arr1, arr2))
print(arr)
print()

print("stack with axis 1")
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print()

print("hstack")
arr = np.hstack((arr1, arr2))
print(arr)
print()

print("vstack")
arr = np.vstack((arr1, arr2))
print(arr)
print()

print("dstack")
arr = np.dstack((arr1, arr2))
print(arr)
print()

print("concatenate")
arr = np.concatenate((arr1, arr2))
print(arr)
print()'''


''''''