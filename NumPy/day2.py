import numpy as np
import time

# size = 10000000
# l1 = range(size)
# l2 = range(size)

# a1 = np.arange(size)
# a2 = np.arange(size)

# start = time.time()
# result = [(x + y) for x, y in zip(l1, l2)] #(x =1, y=1)
# print("Python list took: ", (time.time() - start) * 1000)

# start = time.time()
# result = a1 + a2
# print("Numpy array took: ", (time.time() - start) * 1000)

# a =[1,2,3,4,5] #python list
a = np.array([1,2,3,4,5])
# print(a.dtype)

b = np.array([[1,2,3,4], [5,6,7,8], [3,4,5,6]])

# print(b)
# print(a[3])
# print(b[2])
# print(b[2][2])
# print(b[2,1])
# print(b[-1][-2])
# print(b[-1])
# print(b)
# print(b.size)
# print(a.size)
# print(len(b))
# print(len(a))
# print(b.shape)
# print(b.itemsize)

x = np.zeros(10)
# print(x)

y = np.ones(10)
# print(y)

z = np.empty(4)
# print(z)

z = np.empty((3, 4))
# print(z)

# a1 = np.arange(10)
# print(a1)
# a2 = np.arange(1,10)
# print(a2)
# a3 = np.arange(1,10, 2)
# print(a3)

# print(b.shape)
b1 = b.reshape(2,6)
# print(b1)
b2 = b.reshape(6,2)
# print(b2)
b3 = b.reshape(4,3)
# print(b3)

l1 = np.linspace(1,10, 8)
# print(l1)
print(b.min())
print(b.max())