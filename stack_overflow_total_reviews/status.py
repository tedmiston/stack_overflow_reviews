import json
from collections import OrderedDict

from . import conf
from .cache import cache
from .models import get_queues


def fetch_counts():
    counts_json = '{"close": 9000, "reopen": 142, "suggested-edits": 98, "triage": 68, "helper": 40, "low-quality-posts": 37, "late-answers": 7, "first-posts": 30}'  # noqa
    return counts_json


def get_review_queues_current_status(user=None):
    """
    Which queues have questions/answers/posts/edits available for review?

    https://stackoverflow.com/review
    """

    # only include queues accessible at this user's reputation level
    user_reputation = user.reputation
    queues = get_queues()
    if user is not None:
        queues = (x for x in queues if x.reputation <= user_reputation)

    counts = cache.get_or_update('status', fetch_counts, ttl=conf.CACHE_TTL_QUEUE_STATUS)
    counts = json.loads(counts)

    queue_counts = OrderedDict([
        (queue, counts.get(queue.slug, 0)) for queue in queues])
    return queue_counts
