# to run 
# scrapy crawl imdb_spider -o movies.csv

import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from re import search

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt4154796/']

    def parse(self,response):
        url = "https://www.imdb.com/title/tt4154796/fullcredits"
        yield scrapy.Request(url, callback = self.parse_full_credits)

    def parse_full_credits(self, response):

         
        actor_suffix = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        prefix = "https://www.imdb.com/"
        actor_url = [prefix + suffix for suffix in actor_suffix]
        
        for actor in actor_url:

            yield Request(actor, callback = self.parse_actor_page)

    def parse_actor_page(self,response):
        actor_name = response.css("span.itemprop::text").get()
        
        for movie in response.css("div.filmo-row"):
            movie_or_TV_name = [movie.css("a::text").get()]
        
            yield {
                "actor" : actor_name, 
                "movie_or_TV_name" : movie_or_TV_name
            }
            
        