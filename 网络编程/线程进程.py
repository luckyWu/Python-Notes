import redis
import requests
import re
from bs4 import BeautifulSoup
import lxml
from collections import deque
import asyncio
import aiohttp
from multiprocessing import Process
from threading import Thread
from aiohttp import ClientProxyConnectionError
from asyncio import TimeoutError
db = redis.Redis(host='47.106.211.81', port=6379)


header = {
'Connection': 'Keep-Alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
}

def crawl_kuaidaili():
    # global q
    # 国内高匿代理
    url = 'https://www.kuaidaili.com/free/inha/1/'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    ss = soup.find_all(name='td', attrs={'data-title':'IP'})
    for s in ss:
        ip = s.string
        port = s.next_sibling.next_sibling.string
        res = (ip+':'+port)
        db.rpush('proxy_ip',res)


def crawl_xicidaili():
    url = 'http://www.xicidaili.com/wt/1'
    # global q
    html = requests.get(url, headers=header)
    res = html.text
    # print(res)
    obj = re.compile(
        '<img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
    )
    #         # \s* 匹配空格，起到换行作用
    adds = re.findall(obj, res)
    # print(adds)
    for adress, port in adds:
        result = adress + ':' + port
        # print(result)
        # q.append(result)
        db.rpush('proxy_ip', result)
        # print(q)
# crawl_xicidaili()
url = 'http://www.baidu.com'

async def test(proxy):
    try:
        async with aiohttp.ClientSession() as session:
            try:
                real_proxy = 'http://' + proxy
                async with session.get(url, proxy=real_proxy, timeout=3) as reponse:
                    if reponse.status == 200:
                        print(proxy,'----is valid')
                        # q.append(proxy
            except (ClientProxyConnectionError, TimeoutError, ValueError):
                print(proxy, '------is not valid')
            except:
                print('error')
    except:
        print('pass')

# ip = '180.127.142.62:9999'
import time
def test_run():
    while True:
        if db.llen('proxy_ip')>0:
            ip = db.rpop('proxy_ip')
            ip = ip.decode('utf-8')
            print(ip)
            loop = asyncio.get_event_loop()
            future = asyncio.gather(test(ip))
            loop.run_until_complete(future)
        else:
            print('等待！！！！！！！')
            time.sleep(4)


def get_ip():
    Thread(target=crawl_xicidaili).start()
    Thread(target=crawl_kuaidaili).start()

def run():
    Process(target=get_ip).start()
    Process(target=test_run).start()

if __name__ == '__main__':


    run()


