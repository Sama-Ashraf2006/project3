#!/usr/bin/env python
# coding: utf-8

# In[5]:


#question 1
my_list=[2,3,6]
x=1
for i in my_list:
    x= x*i
print(x)


  


# In[28]:


#question 2
def sort(list1):
  return(sorted(list1, key= lambda x: float(x[1])))
list1 = [(5,4),(9,6),(5,3),(7,1),(8,8)]
print(sort(list1))


# In[7]:


#question 3
d1={'a':100,'b':200 ,'c':300}
d2={'a':300 , 'b':200 , 'd':400}
d3= dict (d1)
d3.update(d2)
for i ,j in d1.items():
    for x ,y in d2.items():
        if i==x:
            d3[i]=(j+y)
d3


# In[8]:


d1={'a':100,'b':200 ,'c':300}
d2={'a':300 , 'b':200 , 'd':400}
d3={}
for i ,j in d1.items():
    for x ,y in d2.items():
        if i==x:
            d3[i]=(j+y)
d3


# In[ ]:


#Question 4
def q4(number):
    d = {}
    for i in range(1,number+1,1):
        print(i)
        d[i] = i*i
    print(d)
    
number = int(input('Please Enter ur number : '))
q4(number)


# In[24]:


#question 5
def sort(tup):
    return(sorted(tup, key= lambda x: float(x[1])))
tup =[('item10', '12.20'), ('item17', '15.10'), ('item5', '24.5')]
print(sort(tup))


# In[41]:


#question 6
x={0,1,2,3,4}
for i in range(5):
    print(i)
x.add(10)
x
x.remove(4)
x


# In[ ]:





# In[ ]:





# In[ ]:




