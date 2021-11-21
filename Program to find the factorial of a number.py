#!/usr/bin/env python
# coding: utf-8

# In[7]:


def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
num=10
print("factorial of", num, "is", factorial(num))


# In[ ]:





# In[ ]:




