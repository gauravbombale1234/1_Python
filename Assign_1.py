# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:08:18 2023

@author: Omsai
"""

import seaborn as sns
import pandas 
import matplotlib.pyplot as plt

df=sns.load_dataset('iris')
df
df.head()

#displot
sns.displot(x='sepal_length',kde=True,bins=6,data=df)

# Box plot
sns.boxplot(df)

#
sns.countplot(x='sepal_length',data=df)

#
plt.hist(x='sepal_length',data=df)

#
sns.kdeplot(x='sepal_length',data=df)

#
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

## joint plot
sns.jointplot(x='sepal_length',y='petal_length',data=df,hue='species')

#
sns.pairplot(df)

#
corr=df.corr()
sns.heatmap(corr)
