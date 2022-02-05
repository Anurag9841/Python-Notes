#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np


# Method to create array using list, tuple ,dictionary

# In[13]:


myarr=np.array([1,2,3,4])


# In[14]:


myarr


# In[15]:


array=np.array([[1,2,3,4],[2,4,6,8]]) #---> creating 2D array


# In[16]:


array


# In[18]:


array.size  #-->returns size of aray


# In[17]:


array.shape  #---> returns the shape of array


# In[19]:


array.dtype  #---> returns the data type of array


# In[20]:


array[0,1]=5  #---> change the value at that particular index of array


# In[21]:


array


# In[22]:


dictarr=np.array({"roll 1": 20,"roll 2": 40})


# In[23]:


dictarr


# In[27]:


tuplearr=np.array((1,2,3,4,5))


# In[28]:


tuplearr


# Creating array using numpy objects like arange,zeros,linspace etc...

# In[58]:


import numpy as np
import random


# array using lispace

# In[59]:


lspace=np.linspace(0,10,5)#---> this function divides number from 0 to 10 in 5 equally spaced points


# In[60]:


lspace


# In[61]:


lspace=np.linspace(0,110,10)


# In[62]:


lspace


# In[63]:


lspace.size


# In[64]:


lspace.shape


# In[65]:


lspace.dtype


# array using arange

# In[66]:


arr=np.arange(10)


# In[67]:


arr


# In[ ]:





# array using zeros

# In[68]:


zero=np.zeros((2,3))


# In[69]:


zero #---> this returns the 2d array of size  2 * 3


# In[70]:


zero1=np.zeros((5,5))


# In[71]:


zero1


# In[79]:


for i in range(0,5):
    for j in range(0,5):
        zero1[i,j]=random.randint(1,100)


# In[80]:


zero1


# In[ ]:




