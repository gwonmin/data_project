#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_excel("아이펠리/20년 10월.xlsx")


# In[9]:


region_df = pd.read_excel("지역정보리스트.xlsx")


# In[10]:


region_df = region_df.drop([0, 1], axis = 0)


# In[11]:


df


# In[12]:


a = set()


# In[13]:


region_df


# In[14]:


시_list = region_df['전국행정동리스트'].str.extract('(\w*시)').dropna(subset = [0])

군_list = region_df['전국행정동리스트'].str.extract('(\w*군)').dropna(subset = [0])


# In[15]:


시_list


# In[16]:


군_list


# In[17]:


df_region = df["주소"].str.extract('(\w*시)|(\w*군)')


# In[18]:


df_region


# In[19]:


df_a = df_region[df_region[1].isna() == True]


# In[20]:


df_a[df_a[0].isna() == True]


# In[21]:


df.iloc[1368]


# In[22]:


시_list = [i for i in df_region.dropna(subset = [0])[0]]

군_list = [i for i in df_region.dropna(subset = [1])[1]]


# In[23]:


시_list


# In[27]:




