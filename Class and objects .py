#!/usr/bin/env python
# coding: utf-8

# Defining Class 

# class number:
#     def sum (self,a,b):
#         return a+b

# In[2]:


t=number()
t.sum(11,20)


# In[3]:


class number:
    def sum(self):
        return self.a+self.b


# In[4]:


n=number()
n.a=100
n.b=200
n.sum()


# In[11]:


class RailWayForm:
    def print(self):
        print(f"This form belongs to {self.name}")
        print(f"The train allocated is {self.train}")


# In[12]:


rail=RailWayForm()
rail.name="Anurag"
rail.train="Bullet"


# In[13]:


rail.print()


# Class attributes---> company and salary

# In[39]:


class Employee:
    company="Google"
    salary=1000


# Instance of class---->harry and rajani

# In[40]:


harry=Employee()
rajni=Employee()
harry.company


# In[41]:


Employee.company="you tube"
harry.company


# In[42]:


harry.salary


# Instance attributes salary ---> 

# In[43]:


harry.salary=2000
rajni.salary=1000


# one more thing to understand when we print harry.salary compiler 1st checks if there is any instance attribute of salary if true then instance attribute is printed ..thus instance attribute priority is more than that of class attributes..

# In[44]:


print(harry.salary)
print(rajni.salary)


# Understanding Self in OOPS
# 
# 
# 
# Using self we are able to make use of instance attribute as well as class attriutes---> in below program we created instance attribute salary and using self.salary we were able to use it in class also we were able to use class attribute company.

# In[52]:


class Employee:
    company="Google"
    def getSalary(self):
        return f"Salary of employee working in {self.company} is {self.salary}"


# In[53]:


emp=Employee()


# creating instance attributes

# In[54]:


emp.salary=1000
emp.getSalary()


# Static Method 

# In[84]:


class Employee:
    company="Youtube"
    salary=250
    def getSalary(self):
        return f"salary of employee working in {self.company} is {self.salary}"
    @staticmethod #---> to mark prints as staticfunction
    def prints():
        return "Thanks"


# In[85]:


anurag=Employee()
anurag.getSalary()


# In[86]:


anurag.prints()


# Constructor In ---> as soon as object is created a special method known as constructor is called

# In[97]:


class student:
    
    def __init__(self,name,roll,subject):
        self.name=name
        self.roll=roll
        self.subject=subject
        print("This is constructor")
    def student_details(self):
        print(f"The name of the student is {self.name}.His roll number is {self.roll}.I am currently studying {self.subject}")


# In[98]:


ram=student("Anurag",10,"Computer Science")
ram.student_details()


# In[ ]:




