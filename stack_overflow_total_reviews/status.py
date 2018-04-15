from collections import OrderedDict

from .models import get_queues


def get_review_queues_current_status():
    """
    Which queues have questions/answers/posts/edits available for review?

    https://stackoverflow.com/review
    """
    queues = get_queues()
    counts = {
        'close': 9000,
        'reopen': 142,
        'suggested-edits': 98,
        'triage': 68,
        'helper': 40,
        'low-quality-posts': 37,
        'late-answers': 7,
        'first-posts': 30,
    }
    queue_counts = OrderedDict([
        (queue, counts.get(queue.slug, 0)) for queue in queues])
    return queue_counts
