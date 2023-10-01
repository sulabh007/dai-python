import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1=pd.read_csv("movies11.csv")
df2=pd.read_csv("movies12.csv",names=['movieId', 'title', 'genres'])
df3=pd.read_csv("movies13.csv",names=['movieId', 'title', 'genres'])

movies_df=pd.concat([df1,df2,df3], axis="rows")

masala_movies_df=movies_df.loc[movies_df['genres'].apply(lambda x: all(genre in x for genre in ['Action', 'Comedy', 'Romance', 'Thriller']))]

print(masala_movies_df)










