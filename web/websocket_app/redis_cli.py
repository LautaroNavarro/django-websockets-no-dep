import redis


class RedisCli:

    instance = None

    @classmethod
    def get(cls):
        if not cls.instance:
            cls.instance = redis.client.StrictRedis(host='redis', port=6379)
        return cls.instance
