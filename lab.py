# sa3 x1

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))#
print(arr)

ar1 = np.array([[1, 2], [3, 4]])
ar2 = np.array([[5, 6], [7, 8]])
ar = np.concatenate((ar1, ar2), axis=1) 
print(ar)#concatenate these two arrays horizontally


a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a = np.stack((a1, a2), axis=1) #first it made tranverse and then concatenated
#stack these two arrays vertically
print(a)
