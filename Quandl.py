#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests, json


# In[181]:


url = "https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker=AAPL&api_key=pEsFgCN47X4-96KiVWNx"


# In[182]:


rawdata = requests.get(url).content


# In[183]:


data = json.loads(rawdata)


# In[184]:


data_keys = data.keys()


# In[185]:


data_keys


# In[186]:


datatable_keys = data['datatable'].keys()


# In[187]:


datatable_keys


# In[188]:


rows = data["datatable"]["data"]


# In[189]:


len(rows)


# In[190]:


columns = data["datatable"]["columns"]


# In[193]:


type(columns)


# In[196]:


columns[:4]


# In[201]:


column_names = []
for col in columns:
    column_names.append(col["name"])


# In[208]:


len(rows[0])


# In[210]:


col_names_with_colon = []
for cname in column_names:
   col_names_with_colon.append(":" + cname)


# In[222]:


col_names_with_colon[:4]

