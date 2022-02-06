#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

# In[8]:


arr=np.arange(10)


# In[9]:


arr


# In[10]:


arr.reshape(2,5) #---> USED TO RESHAPE ARRAY ARR


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


# In[3]:


ide=np.identity(3) #---> used to create the identity matrix of size 3


# In[4]:


ide


# In[5]:


ide.size


# In[6]:


ide.shape


# In[16]:


ide.ravel()#---> ravel is used to create 2d array to 1d array


# In[11]:


Arr=np.arange(12)


# In[12]:


Arr


# In[13]:


Arr.reshape(3,4)#---> reshapes array to array with 3 rows and 4 column


# In[14]:


Arr.reshape(4,3)#--> reshapes array to array with 4 rows and 3 column


# In[15]:


Arr.ravel()#---> create 2D array into 1D array


# Numpy some arguments and methods.

# 2D array

# In[17]:


x=[[1,2,3,4],[5,6,7,8],[9,0,1,2]]


# In[18]:


arr=np.array(x)


# In[19]:


arr


# In[20]:


arr.sum(axis=0)#---> axis=0 is directed to  row of 2D array 
# and sum returns the sum of diff elements of row 
# for eg in above array sum of 1,5,9 = 15 here 1 is element of 1st row
# 5 is element of 2nd row and 9 is element of 3rd row.


# In[21]:


arr.sum(axis=1)#----> axis=1 is directed to column of 2D array
# and sum returns the sum of diff element of column
# for eg in above array sum of 1,2,3,4 = 10 here 1 is element of 1st column
# 2 is element of 2nd col , 3 is element of 3rd col and 4 is element of 4th col.


# In[22]:


arr.T #---> gives transpose of array arr


# In[23]:


arr


# In[24]:


arr.argmax()#---> returns the index of max element in arr


# In[25]:


arr.argmin()#---> returns the index of min element in arr


# In[32]:


arr.argsort(axis=1)#---> sorts each row of array and returns their index


# In[ ]:


arr.argsort(axis=0)#---> sorts each column and returns their index


# In[27]:


arr.argmax(axis=0)#---> returns the max element of each column


# In[28]:


arr.argmax(axis=1)#---> returns the max element of each row


# In[29]:


arr.argmin(axis=0)#---> returns the min element of each column


# In[ ]:


arr.argmin(axis=1)#---> returns the max element of each row


# 1D array

# In[33]:


one = np.array([11,2,5,28,6,7,10])


# In[34]:


one.argmax()


# In[35]:


one.argmin()


# In[36]:


one.argsort()


# Numpy mathematical operation

# In[37]:


arr1=np.identity(3)


# In[38]:


arr1


# In[43]:


x=[[1,2,3],[4,5,6],[7,8,9]]


# In[44]:


arr2=np.array(x)


# In[45]:


arr2


# In[46]:


arr1 + arr2


# In[47]:


arr1 * arr2


# In[48]:


arr2 -arr1


# In[49]:


np.sqrt(arr2)


# In[50]:


arr2.max()


# In[51]:


arr2.min()


# In[52]:


arr.sum()


# In[ ]:




