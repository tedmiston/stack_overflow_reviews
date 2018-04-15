from collections import OrderedDict

from .models import get_queues


def get_reviews_all_time():
    """Reviews given for queues I can access."""
    queues = get_queues()
    review_counts = {
        'suggested-edits': 6,
        'triage': 293,
        'helper': 0,
        'low-quality-posts': 0,
        'late-answers': 8,
        'first-posts': 21,
    }
    review_counts_all_queues = OrderedDict([
        (queue, review_counts.get(queue.slug, 0)) for queue in queues])
    last_updated = '2018-04-14'
    return review_counts_all_queues, last_updated
