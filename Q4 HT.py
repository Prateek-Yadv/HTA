#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import chi2_contingency


# In[7]:


br=pd.read_csv('C:/Users/prate/Downloads/Assignment/HTA/BuyerRatio.csv')
br


# In[15]:


df=br.iloc[:,1:5]


# In[16]:


df


# In[17]:


df.isnull().sum()


# In[ ]:


#Assume Null hyposthesis as Ho  All proportions are equal
# Alternate hypothesis as Ha (Not all Proportions are equal)


# In[18]:


chi2_contingency(df)


# In[8]:


# compare p_value with α = 0.05 (At 5% significance level)


# In[ ]:


#Inference: As (p_value=0..6603) > (α = 0.05); Accept Null Hypothesis i.e.All proportions are equal

