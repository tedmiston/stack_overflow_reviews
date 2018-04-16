import redis

DEFAULT_TTL = 86400


class Cache:

    def __init__(self):
        self._redis = redis.StrictRedis(host='localhost', port=6379, db=0,
                                        decode_responses=True)

    def set(self, key, val, ttl=DEFAULT_TTL):
        self._redis.set(key, val, ex=ttl)

    def get(self, key):
        return self._redis.get(key)

    def get_or_update(self, key, fetch_val, ttl=DEFAULT_TTL):
        val = self._redis.get(key)
        if not val:
            self._redis.set(key, fetch_val(), ttl=ttl)
            val = self._redis.get(key)
        return val


cache = Cache()
