# -*- coding: utf-8 -*-
import scrapy
import json
import jmespath
import re
import pandas as pd

class GmbotSpider(scrapy.Spider):
    name = 'gmbot'
    allowed_domains = ['www.nytimes.com']
    def start_requests(self):   
        companies = pd.read_csv('GM.csv',delimiter = ';',
                                encoding = 'utf-8-sig')['Company'].tolist()
        urls = ['https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/company/%s'
                '?q=&sort=newest&page=601&dom=www.nytimes.com' % company  for company in companies]
        for index,url in enumerate(urls):
            yield scrapy.Request(urls[index], meta = {'priority':index})
 
    
    def parse(self, response):
        company = re.findall(r'company/[\w-]*/?',response.url)[0] # Extract company name
        data = json.loads(response.body)
        item_length = len(jmespath.search('members.items',data))
        if not item_length == 0:
            # Parse the response json file of the first page
            headline = jmespath.search('members.items[*].headline',data)
            date = jmespath.search('members.items[*].add_sort_date',data)
            summary = jmespath.search('members.items[*].summary',data)
            
            for item in zip(company,date,headline,summary):
            # Create a dictionary to store the scraped info
                scraped_info = {'company':company,
                                'date' : item[1][:10],
                                'headline' : item[2],
                                'summary' : item[3]
                            }
                            
                # Yield or give the scraped info to scrapy
                yield scraped_info
        else:
            pass
            
        # Request Next Page ?
        
        # Find the number of items/news in the json file    
        total_pages = int(jmespath.search('members.total_pages',data))
        page = int(jmespath.search('members.page',data))    
        while page <= total_pages:
            # Start a new request with page number increased by 1    
            current_page = re.findall(r'page\=\d+',response.url)[0][5:]
            next_page = str(int(current_page)+1).join(response.url.rsplit(current_page, 1))
            yield scrapy.Request(next_page,callback = self.parse,meta = {'priority':response.meta['priority']})  
    
        pass

