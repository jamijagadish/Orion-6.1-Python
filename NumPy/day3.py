import numpy as np
arr1= np.empty([3, 2], dtype=float, order='F')
# print(arr1)

arr2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr2.sum())
print(arr2.sum(axis=1))
print(arr2.sum(axis=0))

# n1 = np.sqrt(arr2)
# print(n1)

# print(arr2[2][3]+10)
# print(arr2[2][3]-10)
# print(arr2[2][3]*10)
# print(arr2[2][3]/10)

arr3 = np.array([1,2,3,4])
arr4 = np.array([5,6,7,8])

# arr5 = arr3 + arr4
# print(arr5)

d1 = np.dot(arr3, arr4)
# print(d1)

p1 = np.power(arr4, arr3)
# print(p1)

flatArr1 = np.ravel(arr2)
# print(flatArr1)
newArr = flatArr1.reshape(4,3)
# print(newArr)

arr5 = np.array([[1,2,3], [4,5,6], [7,8,9]])
flatArr2 = np.ravel(arr5)
# print(flatArr2)



# Indexing and Slicing in NumPy
# 1. Single Dimensional Array
a1 = np.array([1,2,3,4,5])
# print(a1[2])
# print(a1[-1])
# print(a1[2:4])
# print(a1[2:])
# print(a1[:4])

# 2. Multidimensional Array
a2 = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# print(a2[1])
# print(a2[1][2])
# print(a2[0,1])
# print(a2[0:2, 1:4])
# print(a2[1:, 2:])
# print(a2[:, 2:])

# 3. Boolean Indexing
a3 = np.array([[4,2,5,4,5], [16,7,8,49,10], [141,124,143,144,15]])
# print(a3[a3>5])
# print(a3> 10)

# Iteration in Numpy
# a3 = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# for i in a3:
#     print(i)
#     for j in i:
#         print(j)