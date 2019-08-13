#!/usr/bin/env python
# coding: utf-8

# In[4]:

from __future__ import print_function
import sys
import time


# In[5]:


def coinChange(coin, amount) :
    koin = len(coin)
    if (amount == 0) :
        return 0
    result = 1000
    for coins in coin:
        if (coins <= amount) :
            result = min(result, coinChange(coin, amount - coins) + 1)
    return result
#     print(result)


# In[6]:


# %%time
start = time.time()
amount = int (input("Berapa koin yang ingin ditukar : "))
n = int(input("Ada berapa jenis koin yang tersedia : "))
coin = []
for x in range(n):
    coin.append(int(input("Input koin : ")))
coinChange(coin, amount)

end = time.time()
print(end-start)
