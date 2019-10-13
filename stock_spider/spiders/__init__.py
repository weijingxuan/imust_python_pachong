# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import re
s='男  50岁  博士'
print(re.findall("\d+",s)[0]);