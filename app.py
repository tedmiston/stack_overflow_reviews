"""
Keep track of the number of reviews I've done on Stack Overflow.
"""

from collections import OrderedDict
from typing import NamedTuple


class ReviewQueue(NamedTuple):
    name: str
    slug: str


def get_review_queue_stats_url(queue_name):
    return f'https://stackoverflow.com/review/{queue_name}/stats'


def get_queues():
    """
    All review queues available on the site.

    Queues have increasing reputation requirements, so not every user has
    access to every queue.
    """
    return (
        ReviewQueue('Close Votes', 'close'),
        ReviewQueue('First Posts', 'first-posts'),
        ReviewQueue('Help and Improvement', 'helper'),
        ReviewQueue('Late Answers', 'late-answers'),
        ReviewQueue('Low Quality Posts', 'low-quality-posts'),
        ReviewQueue('Reopen Votes', 'reopen'),
        ReviewQueue('Suggested Edits', 'suggested-edits'),
        ReviewQueue('Triage', 'triage'),
    )


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


def main():
    reviews, last_updated = get_reviews_all_time()

    total_reviews = sum(reviews.values())

    print(f'You have performed {total_reviews} reviews on Stack Overflow as '
          f'of {last_updated}.')

    for queue, count in sorted(reviews.items(),
                               key=lambda x: x[1], reverse=True):
        print(f'{count}\t{queue.name}')


if __name__ == '__main__':
    main()
