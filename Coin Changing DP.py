#!/usr/bin/env python
# coding: utf-8

# In[70]:


# get_ipython().run_line_magic('matplotlib', 'inline')
from __future__ import print_function
import numpy as np
import pandas as pd
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import time


# In[89]:


def change(coin, amount) :
    coin.sort()
    row = len(coin)
    col = amount + 1
    table = (row,col)
    matrix = np.zeros(table)
    
    I = 0
    for I in range(col):  #isi baris ke 0 dengan I semua
        matrix[0][I] = int(I)
    
    i = 1                 # isi sisa matrix
    while (i < row) :
        j = 1
        while (j <col):
            if (j < coin[i]) :
                matrix[i][j] = int(matrix[i-1][j])
            else :
                matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j - coin[i]] + 1))
            j+=1
        i+=1

#     df = pd.DataFrame(matrix)
#     w = col + 10
#     h = row
#     plt.figure(1, figsize=(w, h))
#     tb = plt.table(cellText=matrix, loc=(0,0), cellLoc='center')

#     tc = tb.properties()['child_artists']
#     for cell in tc: 
#         cell.set_height(1.0/row)
#         cell.set_width(1.0/col)

#     ax = plt.gca()
#     ax.set_xticks([])
#     ax.set_yticks([])
# #     ax = sns.heatmap(matrix, annot=True, fmt="f")
#     plt.show()    
        
#     print(matrix)
    print("koin minimum : ", end= " ")
    print(int(matrix[row-1][col-1]))

    a = row - 1             # output koin koin yang dipilih
    b = col - 1
    count = 0
    cek = 0
    print("Koin-koin yang ditukarkan : ", end= " ")
    while (a > 0 and b > 0) :
        if (matrix[a-1][b] == matrix[a][b]) :
            a -= 1
            continue
        print(coin[a], end= " ")
        b -= coin[a]
        amount -= coin[a]
        count += 1
    
    if (count != matrix[row-1][col-1]) :
        print(coin[a])
        amount -= coin[a]

    if (amount != 0) :
        print()
        print("koin tidak bisa ditukar")


# In[87]:


# %%time
start = time.time()
amount = int (input("Berapa koin yang ingin ditukar : "))
if (amount > 0) :
    n = int(input("Ada berapa jenis koin yang tersedia : "))
    coin = []
    for x in range(n):
        coin.append(int(input("Input koin : ")))
    change(coin, amount)
else :
    print("Koin tidak dapat ditukar")
    
end = time.time()
print()
print("Waktu eksekusi : ", end= " ")
print(end - start)

