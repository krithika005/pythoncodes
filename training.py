#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=9
if x%2==0:
    print("Even")
else:
    print("odd")


# In[2]:


x>2


# In[3]:


x%2==0


# In[4]:


x+7.2


# In[9]:


x=-5.8
if x>0:
    print('pos')
elif x<0:
    print('neg')
else:
    print('zero')


# In[10]:


x=5.8
if x>0:
    print('pos')
elif x<0:
    print('neg')
else:
    print('zero')


# In[11]:


x=5.8
if x<0:
    print('pos')
elif x<0:
    print('neg')
else:
    print('zero')


# In[15]:


x=6
if x>0:
    print('pos')
    if x>10:
        print('M')
    elif x>20:
        print('P')
    elif x<10:
        print('K')
    else:
        print('T')
        
        
elif x<0:
    print('neg')
    
    if x<-20:
        print('Q')
    elif x>-10:
        print('C')
    elif x>-30:
        print('Z')
        
        
else:
    print('zero')


# In[17]:


x=input()
if x[0]=='T' or x[0]=='t':
    print('yes')
else:
    print('no')


# In[18]:


x=input()
if x[0]=='T' or x[0]=='t':
    print('yes')
else:
    print('no')


# In[19]:


x=input()
if x[0]=='S' or x[0]=='s':
    print('yes')
else:
    print('no')


# In[21]:


x="Sanjana"
if x[0]=='S' or x[0]=='s':
    print('yes')
else:
    print('no')


# In[ ]:


x=input()
if x[0]=='M' or x[0]=='m':
    print('yes')
else:
    print('no')


# In[31]:


x='tiger'
if x[0].lower()=='t':
    print('yes')
else:
    print('no')


# In[29]:


x='tiger'
if x[0].lower()=='t':
    print('yes')
else:
    print('no')


# In[30]:


if x[0].lower() in ('34', '25'):
    print('yes')
else:
    print('no')


# In[ ]:




