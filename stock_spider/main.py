from scrapy.cmdline import execute

import sys
import os

#调试的一个写法
sys.path.append(os.path.dirname(os.path.abspath(__file__)));
# exec("scrapy","crawl","tonghuashun");
# execute(["scrapy","crawl","tonghuashun"]);
# execute(["scrapy","crawl","tonghuashun"]);
execute(["scrapy","crawl","stock"]);
#前两个参数是固定的，最后一个参数是自己创建的名字

