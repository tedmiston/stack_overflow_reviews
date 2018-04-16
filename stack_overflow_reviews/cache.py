import logging

import redis

from . import conf

log = logging.getLogger(__name__)
logging.basicConfig(level=conf.LOG_LEVEL)


class Cache:

    def __init__(self):
        self._redis = redis.StrictRedis(host=conf.REDIS_HOST,
                                        port=conf.REDIS_PORT,
                                        db=conf.REDIS_DB,
                                        decode_responses=True)

    def set_from_func(self, key, val_func, ttl=conf.CACHE_TTL_DEFAULT):
        val = val_func()
        self._redis.set(key, val, ex=ttl)

    def get(self, key):
        return self._redis.get(key)

    def get_or_update(self, key, fetch_val, ttl=conf.CACHE_TTL_DEFAULT):
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
