#!/usr/bin/env python
# coding: utf-8

# In[7]:


import yfinance as yf
BTC_Ticker=yf.Ticker("BTC-USD")
AXS_Ticker=yf.Ticker("AXS-USD")
ALGO_Ticker=yf.Ticker("ALGO-USD")
SLX_Ticker=yf.Ticker("SLX-USD")
AAVE_Ticker=yf.Ticker("AAVE-USD")


# In[8]:


BTC_Data=BTC_Ticker.history(period="3y")
AXS_Data=AXS_Ticker.history(period="3y")
ALGO_Data=ALGO_Ticker.history(period="3y")
SLX_Data=SLX_Ticker.history(period="3y")
AAVE_Data=AAVE_Ticker.history(period="3y")


# In[15]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
BTC_Data['Open'].plot(label='BTC',figsize=(12,8),title='Open Price')
AXS_Data['Open'].plot(label='AXS')
ALGO_Data['Open'].plot(label='ALGO')
SLX_Data['Open'].plot(label='SLX')
AAVE_Data['Open'].plot(label='AAVE')
plt.legend()


# In[17]:


BTC_Data['Volume'].plot(label='BTC',figsize=(20,15),title='Volume')
AXS_Data['Volume'].plot(label='AXS')
ALGO_Data['Volume'].plot(label='ALGO')
SLX_Data['Volume'].plot(label='SLX')
AAVE_Data['Volume'].plot(label='AAVE')
plt.legend()


# In[18]:


AAVE_Data['Volume'].argmax()


# In[20]:


AAVE_Data.index[125]


# In[21]:


BTC_Data['Total Traded']=BTC_Data['Open']*BTC_Data['Volume']
AXS_Data['Total Traded']=AXS_Data['Open']*AXS_Data['Volume']
ALGO_Data['Total Traded']=ALGO_Data['Open']*ALGO_Data['Volume']
SLX_Data['Total Traded']=SLX_Data['Open']*SLX_Data['Volume']
AAVE_Data['Total Traded']=AAVE_Data['Open']*AAVE_Data['Volume']


# In[22]:


BTC_Data['Total Traded'].plot(label='BTC',figsize=(30,20))
AXS_Data['Total Traded'].plot(label='AXS')
ALGO_Data['Total Traded'].plot(label='ALGO')
SLX_Data['Total Traded'].plot(label='SLX')
AAVE_Data['Total Traded'].plot(label='AAVE')
plt.legend()
plt.ylabel('Total Traded')


# In[23]:


SLX_Data['Total Traded'].index[251]


# In[24]:


SLX_Data['MA50']=SLX_Data['Open'].rolling(50).mean()
SLX_Data['MA150']=SLX_Data['Open'].rolling(150).mean()
SLX_Data[['Open','MA50','MA150']].plot(label='Data',figsize=(16,8))


# In[25]:


from pandas.plotting import scatter_matrix


# In[26]:


car_comp=pd.concat([BTC_Data['Open'],ALGO_Data['Open'],SLX_Data['Open'],AAVE_Data['Open'],AXS_Data['Open']],axis=1)


# In[27]:


car_comp.columns=['BTC_Data Open','AXS_Data Open','ALGO_Data Open','SLX_Data Open','AAVE_Data Open']


# In[28]:


scatter_matrix(car_comp,figsize=(10,10),alpha=0.4,hist_kwds={'bins':50});


# In[29]:


plt.imshow(car_comp,cmap='hot',interpolation='nearest')


# In[ ]:




