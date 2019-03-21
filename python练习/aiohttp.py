"""
同步：阻塞；
异步：不阻塞

async python3.6-- 支持
import asyncio
"""
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(url, pattern=None):
	async with aiohttp.ClientSession() as session:
		html = await fetch(session, url)
		return html

# urls = ['http://www.jd.com/','http://python.org','https://github.com/','http://www.baidu.com','http://www.taobao.com']
urls = ['http://www.mafengwo.cn/travel-scenic-spot/mafengwo/13061.html']*10000000
loop = asyncio.get_event_loop()
futures = asyncio.gather(*[main(url) for url in urls])
futures.add_done_callback(lambda x:print(x.result()))

loop.run_until_complete(futures)
loop.close()