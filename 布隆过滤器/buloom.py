# BloomFilter 是定长的
import time
from pybloom_live import BloomFilter

url1 = 'http://www.baidu.com'
url2 = 'http://qq.com'

bf = BloomFilter(capacity=100000000, error_rate=0.00001) #0.0001: 230M, 0.00001 : 300M
bf.add(url1)
print(url1 in bf)
print(url2 in bf)
time.sleep(30)