
import pandas as pd
df=pd.read_table('http://bit.ly/chiporders'); #by default separator is tab
df1=pd.read_table('http://bit.ly/movieusers',sep="|",header=None);# -*- coding: utf-8 -*-

print(df.columns)

df.rename(columns={'order_id'"new_order_id"})
print(df.columns)

# df.columns=["col1","col2","col3","col4","col5"]
# print(df['col1'])

print(df.head())
print(df.tail())

print(df.head(12))

print(df.info())
print(df.describe())

print(type(df))
print((type(df['quantity'])))
print(df[['quantity','item_name']])

df["newitem_price"]=df['item_price'].map(lambda x:x.replace('$','0'))
print(df.info())
df["newitem_price"]=df['newitem_price'].astype('float')
df["discounted_value"]=df['newitem_price'].map(lambda x:x*0.85)
df["discounted_value"]=df['newitem_price']*0.85
print(df.describe())

#delete the coulumn
df.pop('newitem_price')

df.drop(['newitem_price'],axis=1,inplace=True)

df.drop([2,4,10],axis=0,inplace=True)

print(df[df['discounted_value']>8])
index_num=df[df['discounted_value']>8].index

df.drop(index_num,axis=0,inplace=True)
print(df.shape)



































