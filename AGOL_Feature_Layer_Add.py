#!/usr/bin/env python
# coding: utf-8

# In[2]:


import arcgis


# In[4]:


from arcgis.gis import GIS
gis = GIS()


# In[5]:


map1 = gis.map('Concord, NH')
map1


# In[6]:


# Item Added From Toolbar
# Title: Home Owners' Loan Corporation (HOLC) Neighborhood Redlining Grade | Type: Feature Service | Owner: dianaclavery_uo
item = gis.content.get("ef0f926eb1b146d082c38cc35b53c947")
item


# In[7]:


map1.add_layer(item)
map1


# In[ ]:




