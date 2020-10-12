#!/usr/bin/env python
# coding: utf-8

# In[8]:


is_palindrome = input('Enter a word that you suspect is a palindrome:')
if is_palindrome == is_palindrome[::-1]:
    print('Yes, that is a palindrome!')
else:
    print('No, not a palindrome...') #I had to include an extra line because leaving the user hanging without an answer seemed wrong to me.

