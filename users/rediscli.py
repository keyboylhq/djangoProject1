import redis  # 导包redis

# 生成一个redis的连接池，方便redis客户端的管理与使用
pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)


# db: 指明使用Redis的哪个库，redis有16个库，0-15
# decode_responses： 指明取出的字符串，是否进行解码


def get_redis_cli():
    """每次需要redis客户端，就调用该方法，返回一个客户端"""
    return redis.Redis(connection_pool=pool)