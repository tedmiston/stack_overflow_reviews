import json
from collections import OrderedDict
from datetime import datetime

from . import conf
from .cache import cache
from .models import get_queues


def fetch_reviews():
    counts = '{"suggested-edits": 6, "triage": 293, "helper": 0, "low-quality-posts": 0, "late-answers": 8, "first-posts": 21}'  # noqa
    cache._redis.set('reviews_updated', datetime.now())
    return counts


def get_reviews_all_time():
    """Reviews given for queues I can access."""
    reviews = cache.get_or_update('reviews', fetch_reviews,
                                  ttl=conf.CACHE_TTL_REVIEWS)
    reviews = json.loads(reviews)

    reviews_updated = cache.get('reviews_updated')

    reviews_all_queues = OrderedDict([(queue, reviews.get(queue.slug, 0))
                                      for queue in get_queues()])

    return reviews_all_queues, reviews_updated
