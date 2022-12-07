#!/usr/bin/env python
# coding: utf-8

# ### String formatting in python
# 

# In[3]:


### mostly used methods 


# In[5]:


### 1) .format() method
### you can use format() to do simple positional formatting.


# In[12]:


print('hi, i am {name}'.format(name = 'pallavi'))


# In[14]:


print('I am {age} year old, comming from {location}'.format(age=30, location = 'india'))


# In[17]:


age = 30
location ='india'
print('I am {} year old, comming from {}'.format(age, location))


# In[ ]:





# In[18]:


###3.string interpolation / f-strings


# In[20]:


name= 'Radha' 
print(f'hi, I am {name}')


# In[ ]:





# In[21]:


###3 template String
### you need to import the template class form python build-in string module


# In[26]:


from string import Template

str= Template('hey, $name')
print(str.substitute (name='Ram'))


# In[ ]:




