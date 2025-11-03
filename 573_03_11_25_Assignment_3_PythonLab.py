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


# In[ ]:




