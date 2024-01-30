# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:17:54 2023

@author: Omsai
"""
##########  Seaborn    ####################
import seaborn as sns
import pandas 
import matplotlib.pyplot as plt

sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()

##### plot the graph of sex column in dataframe
sns.countplot(x='sex',data=df)

### graph of survived people and vice versa
# set1 ,set2 ,set3 are color combination
# palette is color
sns.countplot(x='sex',hue='survived',data=df, palette='Set1')

sns.countplot(x='sex',hue='survived',data=df, palette='Set2')

sns.countplot(x='sex',hue='survived',data=df, palette='Set3')

### kdeplot(kernal density estimate plot)
sns.kdeplot(x='age',data=df,color='black')

### Distribution plot
## both kdeplot and histogram in one graph
# bins-> means number of bars
sns.displot(x='age',kde=True,bins=5,data=df)

# only histogram(kde=False)
sns.displot(x='age',kde=False,bins=10,data=df)

###
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],
            palette='Set1',data=df)

##########################################
#########Scatter plot
df=sns.load_dataset('iris')
df.head()

# compare the sepal length & petal length value
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')
"""
Inference :-
        In the above plot, for
            1) setosa : sepal_length<6 & petal_length<2
            2) versicolor : 4.5<sepal_length<7 & 3<=petal_length<5
"""

## joint plot
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

#
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')

#
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

#### Pair plot ### :- shows all possible graphs
sns.pairplot(df)

###   Heap Map   ->shows all possible graphs
corr=df.corr()
sns.heatmap(corr)

"""
Created on Sat May 13 14:34:18 2023

@author: Omsai
"""
from scipy.stats import skew
from scipy.stats import kurtosis
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

cars=pd.read_csv('c:/Gaurav/Q1_a.csv')
cars.columns
cars.describe()


plt.hist(cars.speed)
sns.displot(x='speed',kde=True,bins=6,data=cars)

sns.displot(x='dist',kde=True,bins=6,data=cars)

# Box plot
sns.boxplot(cars.speed)

#
plt.hist(cars.dist)

#
sns.boxplot(cars.dist)


# convert to list
from scipy.stats import skew
from scipy.stats import kurtosis
#skewness
speed=cars['speed'].tolist()
speed
print("Skewness of speed",skew(speed))
#
dist=cars['dist'].tolist()
dist
print("Skewness of speed",skew(dist))

print(skew())


