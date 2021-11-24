#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[16]:


labtat=pd.read_csv('C:/Users/prate/Downloads/Assignment/HTA/LabTAT.csv')
cutlet.head() 


# In[17]:


labtat.isnull().sum()


# In[18]:


labtat.iloc[:,0]


# In[19]:


#Analysis of varaince between more than 2 samples or columns     ----->  Assume Null Hypothesis Ho as No Varaince: All samples TAT population means are same
#u1=u2=u3=u4

#AND Alternate Hypothesis Ha as It has Variance: Atleast one sample TAT population mean is different


# In[20]:


import scipy.stats as stats
stats.f_oneway(labtat.iloc[:,0], labtat.iloc[:,1],labtat.iloc[:,2],labtat.iloc[:,3])


# In[21]:


# compare p_value with α = 0.05 (At 5% significance level)


# In[22]:


#Inference:
    #As (p-value=0) < (α = 0.05); Reject Null Hypothesis,
    #i.e. Atleast one sample TAT population mean is different,
    #Thus there is variance or difference in average Turn Around Time (TAT) of reports of the laboratories on their preferred list.

