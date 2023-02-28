import time
import asyncio
import aiohttp
import blog_spider

semaphore = asyncio.Semaphore(10)   # 并发度

# 利用信号量控制并发度
async def async_spider(url):    # 协程
	async with semaphore:
		print(f"crawl url: {url}")
		async with aiohttp.ClientSession() as session:   # 创建对象
			async with session.get(url) as resp:
				result = await resp.text()
				await asyncio.sleep(5)
				print(f"crawl url: {url}, {len(result)}")


loop = asyncio.get_event_loop()   # 超级循环

tasks = [loop.create_task(async_spider(url)) for url in blog_spider.urls]

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time:", end - start)

