import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr3 = np.vstack((arr1, arr2))
# print(arr3)

arr4 = np.hstack((arr1, arr2))
# print(arr4) #[[1,2,3,4], [1,2,3,4]]

arr5 = np.concatenate((arr1, arr2))
# print(arr5)

arr6 = np.array([[1,2,3,4], [5,6,7,8]])
arr7 = np.array([[9,10,11,12], [13,14,15,16], [17,18,19,20]])

arr8 = np.vstack((arr6, arr7))
# print(arr8)

# arr9 = np.hstack((arr6, arr7))
# print(arr9)

arr10 = np.concatenate((arr6, arr7))
# print(arr10)

# a1 = np.vsplit(arr10,5)
# print(a1)

# a2 = np.hsplit(arr10,2)
# print(a2)

# a3 = np.vsplit(arr6,2)
# a4 = np.vsplit(arr7,2) #not possible
# a4 = np.vsplit(arr7,3)

# a5 = np.hsplit(arr6,2)
# a5 = np.hsplit(arr6,4)
# a5 = np.hsplit(arr6,3) #not possible