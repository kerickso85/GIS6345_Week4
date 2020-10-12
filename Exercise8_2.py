#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arcgis


# In[7]:


my_word = input('Please enter a word >>>')
print('Your word is',my_word)
substring_search = input('What substring or character would you like to search for? >>>')
count=my_word.count(substring_search)
print('That appears',count,'times in the word',my_word)


# In[ ]:





# In[ ]:




