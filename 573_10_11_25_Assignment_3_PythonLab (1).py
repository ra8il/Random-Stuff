#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Pythopn Program to create 1D, 2D,and 3D array from a list and display it using numpy
import numpy as np
arr_1d=np.array([1,2,3,4])
print("1D Array: ", arr_1d)
print("No. of Dimensions: ",arr_1d.ndim)
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print("2D Array:", arr_2d)
print("No. of Dimensions: ",arr_2d.ndim)
arr_3d=np.array([[[1,2,3,4],[2,4,6,8],[1,3,5,7]],[[5,6,7,8],[9,10,11,12],[0,8,6,4]]])
print("3D Array:", arr_3d)
print("No. of Dimensions: ",arr_3d.ndim)
arr=np.array([1,2,3,4,5],ndmin=5)
print("5D Array:", arr)


# In[63]:


#Python Program to implement the array functions of numpy
import numpy as np
arr_zeros=np.zeros(5)
print(arr_zeros)
print(type(arr_zeros)) #numpy= lib, ndarray=class, objects of ndarray
arr_ones=np.ones(5)
print(arr_ones)
print(type(arr_ones))
arr=np.arange(3,10,2)
print(arr)
arr_eye=np.eye(5)
print(arr_eye)
arr_linesp=np.linspace(1,10,num=5)
print(arr_linesp)
arr_rand=np.random.randint(1,100,size=5) #package: np, module:random, randint:function
print(arr_rand)


# In[29]:


#Python program to create data type array and perform array operations on it

import numpy as np
dtarray1=np.arange(4,dtype=np.float_).reshape(2,2) #alias "_"
print("First Array: ",dtarray1)
# dtarrayAlt=np.arange(2,10,2,dtype=np.float_).reshape(2,2)
# print(dtarrayAlt)
dtarray2=np.array([10,12,13,14],dtype="f").reshape(2,2)
print("Second Array: ",dtarray2)
print("Sum of Arrays: ", np.add(dtarray1,dtarray2))
print("Subtraction of Arrays: ", np.subtract(dtarray1,dtarray2))
print("Multiplication of Arrays: ", np.multiply(dtarray1,dtarray2))
print("Division of Arrays: ",np.divide(dtarray1,dtarray2))
print("Matrix dot multiplication of arrays: ", np.dot(dtarray1,dtarray2))
# print("Matrix cross multiplication of arrays: ", np.cross(dtarray1,dtarray2))
# print("Reciprocal of First array: ", np.reciprocal(dtarray1))
print("Reciprocal of Second array: ", np.reciprocal(dtarray2))
print("Reminder of arrays: ", np.mod(dtarray1,dtarray2))
print("Exponential of second array to first array: ", np.power(dtarray2,dtarray1))
print("Transpose of first array: ", dtarray1.T)
print("Transpose of second array: ", dtarray2.T)
print("Maximum element of first array: ", np.max(dtarray1))
print("Maximum element of second array: ", np.max(dtarray2))
print("Minimum element of first array: ", np.min(dtarray1))
print("Minimum element of second array: ", np.min(dtarray2))


# In[10]:


#Python Program to flatten an array
import numpy as np
arr_multi=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print("Given Array: ", arr_multi)
arr_flatten=arr_multi.flatten()
print("Flattened Array: ",arr_flatten)
arr_conditional=np.where(arr_flatten>10)
print(arr_conditional)


# In[ ]:




