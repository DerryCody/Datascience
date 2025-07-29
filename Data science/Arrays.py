import numpy as np
import time
import random

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
print(type(list1))

arr = np.array(list1)
print(arr)
print(type(arr))
'''
list2 = []
t1 = time.time()
for i in range(1,10001):
    list2.append(i)
t2 = time.time()

t3 = time.time()
a1 = np.arange(1,10001)
t4 = time.time()
print(t2-t1)
print(t4-t3)
print(list2)
'''
a2 = np.arange(1,11)
a2 = a2*100
print(a2)
z1 = np.zeros(4,int)
print(z1)
o1 = np.ones((8,4),int)
print(o1)
print(z1.ndim)
print(z1.shape)
print(z1.size)
print(o1.ndim)
print(o1.shape)
print(o1.size)

e = np.arange(2,21,2)
print(e)
d = e.reshape(2,5)
print(d)
nd = d.reshape(10)
print(nd)

nv = np.linspace(10,50,10)
print(nv)

nv2 = np.linspace(10,20,6)
print(nv2)

ra = np.random.randint(1,20,(5,2))
print(ra)

print(np.random.permutation(ra))

bd = np.random.randint(1,20,10)
print(bd)
print(np.sort(bd))