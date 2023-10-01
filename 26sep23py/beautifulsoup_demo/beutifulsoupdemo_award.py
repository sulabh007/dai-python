import requests
from bs4 import BeautifulSoup
import re

url= 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'
response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')


award_containers= html_soup.find_all('tr',style='background:#FAEB86')


for award in award_containers:
    for a in award.find_all('a', href=True):
        val= a['href']



newurl="https://en.wikipedia.org"+val
newresponse = requests.get(newurl)
print(newresponse.text)
newdata=BeautifulSoup(newresponse.text,"html.parser")


title=[]
directedby=[]
releasedate=[]

# pattern = re.compile(r".*.film.*")
pattern = r".*.film.*"

# for award in award_containers:
#     for a in award.find_all('a',href=True):
#         val= a['href']
#         title.append(val)
        
for award in award_containers:
    for a in award.find_all('a',href=True):
        href= a['href']
        #print(href)
    if re.findall(r".*.film.*",href, flags = re.MULTILINE):
        print(a.text)
        title.append(a.text)

    s=award.find('span',class_ = "lister-item-year text-muted unbold" )
    releasedate.append(s.text)
    
print(title)
print(directedby)
print(releasedate)

data={"name":title,"directedby":directedby,"releasedate":releasedate}
import pandas as pd
df=pd.DataFrame[data]























