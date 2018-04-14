# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import json
import re

class DoubanPipeline(object):
    def process_item(self, item, spider):
        item['summary'] = re.sub('\s+',' ',item['summary'])
        if float(item['score']) > 8.0:
            tmp_data = json.dumps(dict(item))
            self.redis.lpush("douban_movie:items",tmp_data)
        return item

    def open_spider(self,spider):
        #连接数据库
        self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)
