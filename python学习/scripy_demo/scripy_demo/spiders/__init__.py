# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

a = "hz123456"

import re

b = re.findall(r'\d{6}', a)[0]
print(b)