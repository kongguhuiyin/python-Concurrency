# python-Concurrency
此存储库仅用作个人学习，保存python多线程学习过程和代码。

课程链接：【【2021最新版】Python 并发编程实战，用多线程、多进程、多协程加速程序运行】 

https://www.bilibili.com/video/BV1bK411A7tV/?share_source=copy_web&amp;vd_source=d6a5a9e1e19bacd0be95f3785d47ed3c



一、运行环境：python 3.7.4  使用conda安装requirements.txt




二、文件说明：

    blog_spider.py为依赖，包含“获取链接”的craw_2函数和获取网页文本的parse函数。

    01.multi_thread_crawl.py：多线程爬虫

    02.producer_consumer_spider.py：生产者-消费者

    03.lock_concurrent.py：线程锁
  
    04.thread_pool.py：线程池
    
    05.flask_thread_pool.py：在Web服务中实现加速
    
    06.thread_process_cpu_bound.py：单线程、多线程、多进程对比CPU密集计算任务的速度
    
    07.flask_process_pool.py：进程池
    
    08.asyncio_spider.py：单线程异步IO，asyncio超级循环
    
    09.async_spider_semaphore.py：利用信号量控制并发度

