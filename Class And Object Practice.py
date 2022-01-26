#!/usr/bin/env python
# coding: utf-8

# Problem 1 ---->Create Class Programmer working in microsoft to store information

# In[1]:


class programmer:
    company="Microsoft"
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def getInfo(self):
        print(f"My name is {self.name}.")
        print(f"I am form {self.address}.")
        print(f"I work for {self.company}.")


# In[2]:


Anu=programmer("Anurag","Dhumbarahi")


# In[3]:


Anu.getInfo()

Problem 2---->Create class calculator capable of finding cube square and sqrt of number
# In[6]:


import math
class calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print("The square of number is ",self.num *self.num)
    def cube(self):
        print("The cube of number is ",math.pow(self.num,3))
    def sqrt(self):
        print("The square root of given number is",math.sqrt(self.num))


# In[7]:


cal=calculator(10)
cal.square()


# In[8]:


cal.cube()


# In[9]:


cal.sqrt()


# Problem 3---->Create class with attribute a and create object attribute 
# and set a to zero does it changes to content of class attribute??

# In[18]:


class check:
    a=100


# In[19]:


attribute=check()


# In[20]:


attribute.a  #-->printing object attributes


# In[21]:


attribute.a=0#-->changing attribute of object


# In[22]:


attribute.a


# In[23]:


check.a #--->changing attribute of object doesnot change class attribute


# Problem 4 ---->Add Static Method to problem no 2

# In[32]:


import math
class calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print("The square of number is ",math.pow(self.num,2))
    def cube(self):
        print("The cube of number is ",math.pow(self.num,3))
    def sqrt(self):
        print("The square root of given number is",math.sqrt(self.num))
    @staticmethod
    def greet():
        print("Hello User")


# In[33]:


cal=calculator(19)
cal.greet()


# In[34]:


cal.sqrt()


# In[35]:


cal.cube()


# In[36]:


cal.square()


# Problem 5 ----> Create class which has method to book ticket ,
# number of seats available and information of train running under Nepal railway

# In[56]:


class Railway:
    def __init__(self,name,seat):
        self.name=name
        self.seat=seat
    def bookTicket(self):
        if(self.seat>0):
            print("you can book seat")
        else:
            print("sorry seat is pack")
    def seatAvailable(self):
        if self.bookTicket() is True:
            print("Yes seat is available")
    def trainInformation(self):
        print(f"The train that you are going to ride is {self.name}")


# In[57]:


Rail=Railway("Nepal Express",20)


# In[58]:


Rail.bookTicket()


# In[59]:


Rail.seatAvailable()


# In[60]:


Rail.trainInformation()

