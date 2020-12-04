                      # bloomfilter

1. 先去这个网站下载`bitarray`这个依赖 `https://www.lfd.uci.edu/~gohlke/pythonlibs/#bitarray`

   直接安装会报错`error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": https://visualstudio.microsoft.com/downloads/`

2. 安装`wheel`文件, 防止我们主动安装报这样的错误`pip3 install bitarray-1.1.0-cp36-cp36m-win_amd64.whl`

3. `pip3 install pybloom_live`



```
# BloomFilter 是定长的
from pybloom_live import BloomFilter

url1 = 'http://www.baidu.com'
url2 = 'http://qq.com'
#capacity: 定容数量,error_rate：错误率（选填) #0.0001: 230M, 0.00001 : 300M
bf = BloomFilter(capacity=1000, error_rate=0.001)
bf.add(url1)
print(url1 in bf)
print(url2 in bf)
```





