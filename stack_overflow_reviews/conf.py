import configparser
import logging

cfg = configparser.ConfigParser()
cfg.read('config.ini')

LOG_LEVEL = getattr(logging, cfg['DEFAULT']['log_level'])

STACK_OVERFLOW_USER_ID = cfg.getint('stack_overflow', 'user_id')

CACHE_TTL_DEFAULT = cfg.getint('cache', 'ttl_default')
CACHE_TTL_REVIEWS = cfg.getint('cache', 'ttl_reviews')
CACHE_TTL_QUEUE_STATUS = cfg.getint('cache', 'ttl_queue_status')
CACHE_TTL_REPUTATION = cfg.getint('cache', 'ttl_reputation')
