import redis
r = redis.Redis()
from redis.exceptions import RedisError


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        r.ping()  # 发送ping命令，返回PONG表示连接成功
        print("Redis 连接成功！")
    except RedisError as e:
        print(f"Redis 连接失败：{e}")