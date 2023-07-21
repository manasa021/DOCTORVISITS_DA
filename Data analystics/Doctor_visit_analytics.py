#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello welcome to the iBM skillsbuild project")


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# # Read the dataset

# In[4]:


df=pd.read_csv("DoctorVisits - DA.csv")


# In[7]:


df.head(15)


# # Display complete information about the columns of the dataset such as Column name,Count, Data type and overall memory usage

# In[8]:


df.info()


# # Find out the total no:of people based on their count of illeness

# In[9]:


df["illness"].value_counts()


# In[10]:


df["gender"].value_counts()


# # Visualize and analyse the maximum, minimum and medium income

# In[11]:


y=list(df.income)
plt.boxplot(y)
plt.show()


# # Find out the no of days of reduced activity of male and female seperatly due to illenes

# In[12]:


df.groupby(['gender', 'reduced']).mean()


# # Visualize is there is any missing values in the dataset based on a heat map

# In[13]:


#missing values
sns.heatmap(df.isnull(),cbar=False,cmap="viridis")


# # Find out the correlation between variables in the given dataset correlation between different variables

# In[14]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')


# # Analyse how the income of a patient effects the no of visits to the hospital

# In[15]:


#relation between income and visits
plt.figure(figsize=(10,10))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')


# # Count and visualize the number of males and females effected by illness

# In[16]:


#No: of male and female effected by illness
sns.histplot(df.gender,bins=2)


# # Visualize the percentage of people getting govt health Insurance due to low income, due to old age and also the percentage of people having private health insurance

# In[17]:


# % of people getting govt Insurance due to low income
label=['yes','no']
Y=df[df['freepoor']=='yes']
N=df[df['freepoor']=='no']
x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt Insurance due to low income ")
plt.show()
# % of people having private Insurance
Y=df[df['private']=='yes']
N=df[df['private']=='no']
x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people having private Insurance ")
plt.show()
# % of people getting govt Insurance due to old age, disability or veteram status
Y=df[df['freerepat']=='yes']
N=df[df['freerepat']=='no']
x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt Insurance due to old age, disability or veteram status ")
plt.show()


# # Plot a horizontal bar chart to analyze the reduced days of activity due to illness based on Gender

# In[19]:


db=df.groupby('gender')['reduced'].sum().to_frame().reset_index()
#Creating the bar chart
plt.barh(db['gender'],db['reduced'],color=['cornflowerblue','lightseagreen'])
#Adding the aesthetics
plt.title('Bar Chart')
plt.xlabel('Reduced activity')
plt.ylabel('gender')
#Show the plot
plt.show()


# In[ ]:




