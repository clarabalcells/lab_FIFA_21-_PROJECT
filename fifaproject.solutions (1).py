#!/usr/bin/env python
# coding: utf-8

# In[1]:


#During this afternoon session, each member of the group must write a function which:

#takes a dataframe as input
#perform the data cleaning operations on the assigned columns
#return a new cleaned dataframe.
#Then put all you group member functions into the group jupyter notebook.

#BONUS
#Try to create a new function called preprocess which"

#takes a dataframe as input
#call all the other group member functions and apply them to the starting dataframe
#return a clean dataframe.


# In[1]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 11

df = pd.read_csv('fifa21_train.csv')

df_num = df.select_dtypes(include=np.number)
df_cat =df.select_dtypes(include=object)

df_num_columns = df_num.columns.tolist()
df_cat_columns = df_cat.columns.tolist()

#print('These are the numerical columns: ', df_num_columns)

#print('These are the categorical columns: ', df_cat_columns)

df.head(200)


# In[16]:


#df_na = df[['Club', 'Position', 'Joined', 'Loan Date End', 'Volleys', 'Curve', 'Agility', 'Balance', 'Jumping','Interceptions', 'Positioning', 'Vision','Composure','Sliding Tackle', 'A/W', 'D/W']]
df.isna().sum()


# In[17]:


df_no_na = df.dropna(subset = ['Club', 'Position', 'Joined', 'Volleys', 'Curve', 'Agility', 'Balance', 'Jumping','Interceptions', 'Positioning', 'Vision','Sliding Tackle', 'A/W', 'D/W', 'Composure'])
df_no_na = df_no_na.drop('Loan Date End', axis=1)
df_no_na.isna().sum()


# In[18]:


print('The shape without the non available values is:', df_no_na.shape)

print('The shape with the available values is:', df.shape)


# In[15]:


df.shape


# In[20]:


df_no_na.head(200)


# In[22]:


df1 = df_no_na[['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'CB', 'RCB', 'RB', 'GK', 'OVA']]
df1.head()


# In[23]:


df1.dtypes


# In[24]:


# #def parse(x):
#    try:
#        return pd.eval(x) 
#    except ValueError:
#        return 'ERROR'
    
#df2 = df1.apply(parse)


# In[25]:


df2 = df.dropna(axis='columns')

#df2.head(100)

df2.isna().sum()
df2.shape


# In[26]:


def clean_data(df):
    data_frame = df.copy()
    df_clean = data_frame.dropna(axis='columns')
    return df_clean.head(200)

clean_data(df)


# In[27]:


best_teams = df.sort_values(by = 'Growth', ascending=False)

best_teams


# In[28]:


type(df.iloc[0])


# In[29]:


best_attack = df.sort_values(by = 'Attacking', ascending=False)
best_attack


# In[30]:


best_skill = df.sort_values(by = 'Skill', ascending=False)
best_skill


# In[31]:


best_heading_accuracy = df.sort_values(by = 'Heading Accuracy', ascending=False)
best_heading_accuracy


# In[34]:


best_finishing = df.sort_values(by = 'Finishing', ascending=False)
best_finishing


# In[35]:


best_gk = df.sort_values(by = 'Skill', ascending=False); df.sort_values (by = 'BP',ascending=False)

best_gk


# In[ ]:





# In[ ]:




