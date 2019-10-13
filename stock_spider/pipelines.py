# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time

class StockSpiderPipeline(object):
    def process_item(self, item, spider):
        return item
class StockPipeline(object):
    def __init__(self):
        self.file=open("executive_prep.csv","a+");#a+:拿到文件的读写权限，没有的话直接写，有的话追加写
    def process_item(self, item, spider):
        # 类加载时要创建一个文件
        # 判断一个文件是否为空，为空则直接写
        #不为空那么我就追加写文件
        if os.path.getsize("executive_prep.csv") and (item not in self.file):
            #开始写文件
            self.write_content(item);
        else:
            self.file.write("高管姓名，性别，年龄，股票代码，职位\n");
        self.file.flush();
        return item;

    def write_content(self,item):
        names = item["names"];
        sexes = item["sexes"];
        ages = item["ages"];
        codes = item["codes"];
        leaders = item["leaders"];
        #此时获取到所有的数据了
        result="";
        for i in range(len(names)):
            result=names[i]+","+sexes[i]+","+ages[i]+","+codes[i]+","+leaders[i]+"\n";
            self.file.write(result);



