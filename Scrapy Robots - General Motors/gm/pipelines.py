# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os.path

class GmPipeline(object):
    def process_item(self, item, spider):
        filename = item['company'] + '2.csv'
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filename,'a',newline = '',encoding ='utf-8-sig') as f:
            writer = csv.writer(f)
            # write only selected elements 
            row = [item['date'], item['headline'],item['summary']]
            writer.writerow(row)
        
        
        return item
