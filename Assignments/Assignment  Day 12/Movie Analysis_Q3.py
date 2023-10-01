import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1=pd.read_csv("movies11.csv")
df2=pd.read_csv("movies12.csv",names=['movieId', 'title', 'genres'])
df3=pd.read_csv("movies13.csv",names=['movieId', 'title', 'genres'])
rating_df=pd.read_csv("rating11.csv")
movies_df=pd.concat([df1,df2,df3], axis="rows")

s=rating_df.groupby('movieId')['rating'].mean()
average_rating=s.to_frame()

combine=movies_df.merge(average_rating, on="movieId",how='right')

list1=(combine.assign(genres = combine['genres'].str.split('|'))
         .explode('genres')
         .groupby(['genres',"rating"])
         .size()
         .sort_index(level=[1,0], ascending=[True, False])
         .reset_index(name='count')
         )

average=list1.groupby('genres')['rating'].mean()

average=average.reset_index()
plt.pie(average['rating'],labels=average['genres'],autopct='%1.1f%%', pctdistance=0.82,shadow=True,textprops={'fontsize':35},startangle=90)
