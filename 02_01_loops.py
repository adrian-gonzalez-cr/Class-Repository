#!/usr/bin/env python
# coding: utf-8

# # 02_01: Warmup with Python Loops

# In[55]:


import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

get_ipython().run_line_magic('matplotlib', 'inline')


# In[56]:


for i in range(0, 10):
    print(i)


# In[57]:


for i in range(5):
    print(i)


# In[58]:


for i in range(0, 10, 2):
    print(i)


# In[59]:


# loop over all possible counts for each coin (summing up to <= 1$);
# if the total amount is exactly $1, add current counts to "combinations"

combinations = []

for count_100 in range(1+1):
    for count_50 in range(2+1):
        for count_25 in range(4+1):
            for count_10 in range(10+1):
                for count_5 in range(20+1):
                    for count_1 in range(100+1):
                        if 100*count_100 + 50*count_50 + 25*count_25 + 10*count_10 + 5*count_5 + count_1 == 100:
                            combinations.append([count_100, count_50, count_25, count_10, count_5, count_1])


# In[60]:


combinations


# In[61]:


len(combinations)


# In[62]:


for count_25 in range(4+1):
    print(count_25)


# In[63]:


for amount_25 in range(0, 100+1, 25):
    print(amount_25)


# In[64]:


# loop over all possible $ amount for each coin (summing up to <= 1$);
# if the total amount is <= $1, add current amounts to "combinations_amounts",
# since we can always make up the difference with pennies

combinations_amounts = []

for amount_100 in range(0, 100+1, 100):
    for amount_50 in range(0, 100+1, 50):
        for amount_25 in range(0, 100+1, 25):
            for amount_10 in range(0, 100+1, 10):
                for amount_5 in range(0, 100+1, 5):
                    total_so_far = amount_100 + amount_50 + amount_25 + amount_10 + amount_5
                    
                    if total_so_far <= 100:
                        combinations_amounts.append([amount_100, amount_50, amount_25, amount_10, amount_5,
                                                     100 - total_so_far])


# In[65]:


combinations_amounts


# In[66]:


len(combinations_amounts) 


# In[67]:


# same as above, but now as a function that takes arbitrary total

def find_combinations(total):
    combinations_amounts = []

    for amount_100 in range(0, total+1, 100):
        for amount_50 in range(0, total+1, 50):
            for amount_25 in range(0, total+1, 25):
                for amount_10 in range(0, total+1, 10):
                    for amount_5 in range(0, total+1, 5):
                        total_so_far = amount_100 + amount_50 + amount_25 + amount_10 + amount_5

                        if total_so_far <= total:
                            combinations_amounts.append([amount_100, amount_50, amount_25, amount_10, amount_5,
                                                         total - total_so_far])
    
    return combinations_amounts


# In[68]:


len(find_combinations(200))


# In[69]:


len(find_combinations(400))


# In[70]:


totals = range(100, 600, 100)
lengths = [len(find_combinations(total)) for total in totals]


# In[71]:


pp.plot(totals, lengths)


# In[ ]:




