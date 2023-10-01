import pandas as pd

df1=pd.read_csv("movies11.csv")
df2=pd.read_csv("movies12.csv",names=['movieId', 'title', 'genres'])
df3=pd.read_csv("movies13.csv",names=['movieId', 'title', 'genres'])

movies=pd.concat([df1,df2,df3], axis="rows")


result2=movies[movies['genres'].apply(lambda x: all(genre in x for genre in ['Action', 'Adventure', 'Romance', 'Thriller']))]