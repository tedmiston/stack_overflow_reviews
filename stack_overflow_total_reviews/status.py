import json
from collections import OrderedDict

from .models import get_queues


def fetch_counts():
    counts_json = '{"close": 9000, "reopen": 142, "suggested-edits": 98, "triage": 68, "helper": 40, "low-quality-posts": 37, "late-answers": 7, "first-posts": 30}'  # noqa
    counts = json.loads(counts_json)
    return counts


def get_review_queues_current_status():
    """
    Which queues have questions/answers/posts/edits available for review?

    https://stackoverflow.com/review
    """
    queues = get_queues()
    counts = fetch_counts()
    queue_counts = OrderedDict([
        (queue, counts.get(queue.slug, 0)) for queue in queues])
    return queue_counts