import math
import flask
import json
from concurrent.futures import ProcessPoolExecutor


app = flask.Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    result = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, result)))


if __name__ == "__main__":
    process_pool = ProcessPoolExecutor()   # 进程池的定义与线程池不同，必须放在所有函数的最下面（所有函数都必须定义完成）
    app.run()
