import requests
from bs4 import BeautifulSoup
import re

url= 'https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-01'
response = requests.get(url)
print(response.text)

html_soup = BeautifulSoup(response.text, 'html.parser')

type(html_soup)
print(html_soup)

movie_containers= html_soup.find_all('div', class_="lister-item mode-advanced")

print(type(movie_containers))
print(len(movie_containers))

first_movie=movie_containers[0]
print(first_movie)

h3=first_movie.h3.find_all("a")
# h3[1]
print(first_movie.h3)
print(first_movie.h3.a)
print(first_movie.h3.a.text)

s=first_movie.find('span', class_ = "lister-item-year text-muted unbold")
print(s)
print(s.text)

print(first_movie.strong.text)

second_movie=movie_containers[1]
print(second_movie.h3.a.text)


names=[]
rating=[]
years=[]

for movie in movie_containers:
    names.append(movie.h3.a.text)
    if movie.strong!=None:
        rating.append(movie.strong.text)
    else:
        rating.append(0)
        
    s=movie.find('span',class_ = "lister-item-year text-muted unbold" )
    years.append(s.text)
    
print(names)
print(rating)
print(years)

data={"name":names,"rating":rating,"years":years}
import pandas as pd
df=pd.DataFrame[data]























