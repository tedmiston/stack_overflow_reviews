import logging

import redis

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

DEFAULT_TTL = 86400


class Cache:

    def __init__(self):
        self._redis = redis.StrictRedis(host='localhost', port=6379, db=0,
                                        decode_responses=True)

    def set_from_func(self, key, val_func, ttl=DEFAULT_TTL):
        val = val_func()
        self._redis.set(key, val, ex=ttl)

    def get(self, key):
        return self._redis.get(key)

    def get_or_update(self, key, fetch_val, ttl=DEFAULT_TTL):
        val = self.get(key)
        if val is not None:
            expires_in = self._redis.ttl(key)
            log.debug(f'{key} cache hit (expires in {expires_in} seconds)')
        else:
            log.debug(f'{key} cache miss (fetching)')
            self.set_from_func(key, fetch_val, ttl=ttl)
            val = self.get(key)
        return val


cache = Cache()
