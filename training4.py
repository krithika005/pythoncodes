#!/usr/bin/env python
# coding: utf-8

# In[9]:


x=5
while x<10:
    print('yes')
    x=x+1


# In[10]:


y=[10, 20, 30, 40, 50]
y


# In[11]:


y[0]


# In[12]:


y[4]


# In[14]:


y[2]+5


# In[16]:


y[2]+y[4]


# In[17]:


y*2


# In[18]:


for i in y:
    print(i)


# In[19]:


for i in y:
    print(i*4)


# In[33]:


inr=[]
for i in y:
    print(i*4)
    


# In[44]:


inr=[]
for i in y:
    inr.append(i*85)
    


# In[45]:


inr


# In[35]:


num=[31, 45, 66, 73, 83, 48, 59, 38, 29, 30, 10]
num


# In[40]:


even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)


# In[41]:


even


# In[42]:


odd


# In[46]:


num=[39, 45, 66, 93, 90, 78, 67, 87, 89, 93, 25, 59, 49, 91]
num


# In[50]:


for i in range(len(num)):
    if num[i] == 49:
        num[i] = 41
        
print(num)


# In[53]:


h=[]
for i in num:
    a=str(i)
    b=a.replace('9', '1')
    c=int(b)
    h.append(c)


# In[54]:


h


# In[ ]:




