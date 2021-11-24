#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import chi2_contingency


# In[10]:


cof=pd.read_csv('C:/Users/prate/Downloads/Assignment/HTA/Costomer+OrderForm.csv')
cof.head


# In[17]:


cof['Phillippines'].value_counts(),cof['Indonesia'].value_counts(),cof['Malta'].value_counts(),cof['India'].value_counts()


# In[5]:


cof.isnull().sum()


# In[18]:


chi2_contingency([[271,267,269,280],[29,33,31,20]])


# In[ ]:


#Assume Null Hypothesis as Ho: Independence of categorical variables (customer order forms defective % does not varies by centre) Thus, Alternative hypothesis as Ha Dependence of categorical variables (customer order forms defective % varies by centre)


# In[8]:


# compare p_value with α = 0.05 (At 5% significance level)


# In[ ]:



#Inference: As (p_value = 0.2771) > (α = 0.05); Accept Null Hypthesis i.e. Independence of categorical variables Thus, customer order forms defective % does not varies by centre

