# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class GbCrawlerPipeline(object):

    def __init__(self):
        self.csvwriter = csv.writer(open("GmarketBestsellers.csv", "w"))
        self.csvwriter.writerow(["title","o_price","s_price","discount_rate"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["o_price"])
        row.append(item["s_price"])
        row.append(item["discount_rate"])
        self.csvwriter.writerow(row)
        return item
