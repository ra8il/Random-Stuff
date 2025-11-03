#!/usr/bin/env python
# coding: utf-8

# In[30]:


#program to implement class concepts
class student:
    programme="BCA"
    def __init__(self,eno,name):
        self.eno=eno
        self.name=name
st1=student("573","S")
print("Enrollment No.: ",st1.eno)
print("Name:",st1.name)
print(st1.programme)


# In[31]:


#program to implement class concepts
class student:
    programme="BCA"
    def __init__(self,eno,name):
        self.eno=eno
        self.name=name
    @staticmethod
    def info(sem):
        return sem
    @classmethod
    def fee_data(self,fee):
        self.fee=fee
        return fee
st1=student("573","S")
print("Enrollment No.: ",st1.eno)
print("Name:",st1.name)
print("Programme:",st1.programme)
print("Sem:", student.info("III"))
print("Fee:",st1.fee_data("35000"))


# In[39]:


#program to implement inheritance in python
class lang_info:
    def intro(self):
        print("Python is a multipurpose programming language")
class lang_data(lang_info):
    def uses(self):
        print("Python can be used to develop high level applications")
ld=lang_data()
ld.intro()
ld.uses()


# In[45]:


#program to implement multi-level inheritance in python
class lang_info:
    def intro(self):
        print("Python is a multipurpose programming language")
class lang_data():
    def uses(self):
        print("Python can be used to develop high level applications")
class lang_platform(lang_info,lang_data):
    def framework(self):
        print("Python supports several frameworks like Jupyter Notebook, VS Code, and Spyder")
lp=lang_platform()
lp.intro()
lp.uses()
lp.framework()


# In[1]:


#programme to implement file operation (read and write) in python 
import os 
fp=open("myfile.txt","w") 
fp.writelines("File handling is an essential component of python. \nIt can be used to perform general file operations") 
fp.close() 
fp=open("myfile.txt","r") 
print(fp.read()) 
fp.close()


# In[5]:


#programme to implement file operation (write and then read "w+ mode") in python 
import os 
fp=open("myfile.txt","w+") 
fp.writelines("File handling is an essential component of python. \nIt can be used to perform general file operations")
fp.seek(0)
print(fp.read()) 
fp.close()


# In[ ]:




