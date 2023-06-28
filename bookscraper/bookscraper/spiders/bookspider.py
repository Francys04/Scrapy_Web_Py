# default create scrapy run a class for extract the data from (site.com)
# the class contain name of file , titledomain and url of the site

import scrapy
from bookscraper.items import BookItem
import random

#import bookitem
class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']
    
    # custom settings from wxport file format default
    custom_settings = {
        'FEEDS': { 
            'booksdata.json': { 'format': 'json','overwrite': True}}
        }
    
    
# source of product of data
#for scrapy shell use commands for evrey data need in db name, price, url 
    def parse(self, response):
        books = response.css('article.product_pod')  
        # loops back and after next seleect product and all pages is done will be stop
        # # start main page
        for book in books:
            #inspect the buttom next pages
            relative_url = book.css('h3 a ::attr(href)').get()
                    
        # if not exist next page give is not None, create a new page from url
        # check pages if contains in catalogue
            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url  
                # call details of evrey product parse_book_page
            yield response.follow(book_url, callback=self.parse_book_page)

        ## Next Page        
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page 
                # call itself if no more pages
            yield response.follow(next_page_url, callback=self.parse)
# create fun for evrey product
    def parse_book_page(self, response):
 
        table_rows = response.css("table tr")
        # create table of information of product use response.css
        #specify bookitem
        # book_item = BookItem()
        
    def parse_book_page(self, response):
        book = response.css("div.product_main")[0]
        table_rows = response.css("table tr")
        book_item = BookItem()
        book_item['url'] = response.url
        book_item['title'] = book.css("h1 ::text").get()
        book_item['upc'] = table_rows[0].css("td ::text").get()
        book_item['product_type'] = table_rows[1].css("td ::text").get()
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get()
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get()
        book_item['tax'] = table_rows[4].css("td ::text").get()
        book_item['availability'] = table_rows[5].css("td ::text").get()
        book_item['num_reviews'] = table_rows[6].css("td ::text").get()
        book_item['stars'] = book.css("p.star-rating").attrib['class']
        book_item['category'] = book.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['description'] = book.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        book_item['price'] = book.css('p.price_color ::text').get()
        yield book_item