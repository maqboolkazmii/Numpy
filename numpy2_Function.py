#!/usr/bin/env python
# coding: utf-8

# # Numpy Function

# In[1]:


import numpy as np


# # Arange()
# np.arange=(start,end, steps)  it gaves values in given range by given steps. last digit cant print

# In[2]:



array=np.arange(2,12)
print(array)


# # Linspace()
# linespace(start, stop, numberOf values)
# it gives number of values in given range

# In[3]:


np.linspace(1,5,6)


# # Reshape()
# reshape is used to convart 1d array into 2d 3d array. frist we shoud know about size of array to reshape

# In[4]:


array.reshape(2,5)


# In[5]:


ary2d=np.arange(1,11).reshape(5,2)
print(ary2d)


# In[6]:


#conert 1d to 3d
#array.reshape(3d,2d,1d) and product must be equal to size of 1d array
ary1d=np.arange(1,17)
print(ary1d)
ary1d.size


# In[7]:


mulD=ary1d.reshape(2,2,4)
print(mulD)


# # Ravel()
# convert multi dimensional array into id

# In[8]:


mulD.ravel()


# # Flatten
# 

# In[9]:


mulD.flatten()


# # Transpose

# In[10]:


m=np.array([[1,2],
            [9,8]])
mul=m.transpose()
print(m)
print(mul)


# In[11]:


m.T


# In[ ]:





# In[ ]:




