import pandas as pd

df1=pd.read_csv("movies11.csv")
df2=pd.read_csv("movies12.csv",names=['movieId', 'title', 'genres'])
df3=pd.read_csv("movies13.csv",names=['movieId', 'title', 'genres'])

movies=pd.concat([df1,df2,df3], axis="rows")

 
result=movies[(movies['genres'].str.contains('Action')) & (movies['genres'].str.contains('Romance') & movies['genres'].str.contains('Comedy')) & (movies['genres'].str.contains('Thriller'))]

