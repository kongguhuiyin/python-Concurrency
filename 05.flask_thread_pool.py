import flask
import json
import time
import threading
from concurrent.futures import ThreadPoolExecutor


# 在Web服务中实现加速
app = flask.Flask(__name__)
pool = ThreadPoolExecutor()   # 创建一个全局线程池


def read_file():
	time.sleep(0.1)
	return "file result"

def read_api():
	time.sleep(0.2)
	return "api result"


def read_db():
	time.sleep(0.3)
	return "db result"


@app.route("/")
def index():
	result_file = pool.submit(read_file)
	result_db = pool.submit(read_db)
	result_api = pool.submit(read_api)
	
	return json.dumps({
		"result_file": result_file.result(),   # 使用线程池可以加速
		"result_db": result_db.result(),       # 原本单线程需要100+200+300=600毫秒，并发执行后仅需300毫秒(不计入其他运行时间)
		"result_api": result_api.result(),
	})


if __name__ == "__main__":
	app.run()


