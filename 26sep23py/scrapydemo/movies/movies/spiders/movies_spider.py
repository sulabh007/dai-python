import scrapy
import time
import requests
 
class MoviesSpider(scrapy.Spider):
    name="movies"
    start_urls=['https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-01']
    
    def parse(self,response):
        data={}
        data['MovieName']=response.css('h3 a::text').extract()
        data['Rating']=response.css("strong::text").extract()
        data['Year']=response.css("span.lister-item-year::text").extract()
        yield data

        
        # for ln in response.css('div', class_="lister-item mode-advanced").extract():
        #     url=response.urljoin(ln)
        #     print(url)
            
          
    # def parse_titles(self,response):
    #       for sel in response.css('html').extract():
    #           data={}
    #           data['MovieName']=response.css('h3 a::text').extract()
    #           data['Rating']=response.css("strong::text").extract()
    #           data['Year']=response.css("span.lister-item-year::text").extract()
    #           yield data
