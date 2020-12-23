# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
" pour afficher le max des colone de la date set"

## Exploration des données
pd.options.display.max_columns= None
df=pd.read_csv('housing.csv')
df.head()
df.info()
df['ocean_proximity']
df['longitude']

## Changer le type de certain colone
df= df.astype({'ocean_proximity':'category'})
df.info()

df[df['median_house_value']>100000]

df['rooms_par_households']=df['total_rooms']/df['households']
df.info()
df['rooms_par_households']
df['Bedrooms_par_households']=df['total_bedrooms']/df['households']
df.info()
df['Bedrooms_par_households']

df['population_par_households']=df['population']/df['households']
df.info()

df=df.drop(['latitude'],axis=1)
df.info()
df=df.drop(['longitude'],axis=1)
df.info()

df.describe()

# La representation graphique
df.hist(bins=50,figsize=(20,25))
plt.show()
df['ocean_proximity'].value_counts().plot(kind='bar')

#Etude de la corélation entre les variables
corr_matrix = df.corr()
print(corr_matrix)
corr_matrix['median_house_value'].sort_values(ascending=False)
corr_matrix['total_rooms'].sort_values(ascending=False)
print(corr_matrix['median_house_value'] )

#corr_matrix['median_house_value'].sort_values(asc)
cmap=sns.diverging_palette(220, 10,as_cmap=True)
sns.heatmap(corr_matrix,cmap=cmap,cbar_kws={"shrink" : .5},linewidths=.5)

#Preparation des données 
print(df.describe()["median_income"])
print(df['median_house_value'].hist(bins=50))
 
from sklearn.model_selection import train_test_split
train_set, test_set=train_test_split(df,test_size=0.1,random_state=42)
print(train_set)
print(test_set)
price_train=train_set['median_house_value']
price_test=test_set['median_house_value']
train_set=train_set.drop(['median_house_value'],axis=1)
print(train_set)
test_set=test_set.drop(['median_house_value'],axis=1)
print(test_set)
print(price_train)
