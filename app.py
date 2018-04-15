"""
Keep track of the number of reviews I've done on Stack Overflow.
"""

from collections import OrderedDict


def get_review_queue_stats_url(queue_name):
    return f'https://stackoverflow.com/review/{queue_name}/stats'


def get_queues():
    """
    All review queues available on the site.

    Queues have increasing reputation requirements, so not every user has
    access to every queue.
    """
    return (
        'close',
        'reopen',
        'suggested-edits',
        'triage',
        'helper',
        'low-quality-posts',
        'late-answers',
        'first-posts',
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
        (queue, review_counts.get(queue, 0)) for queue in queues])
    last_updated = '2018-04-14'
    return review_counts_all_queues, last_updated


def main():
    reviews, last_updated = get_reviews_all_time()

    total_reviews = sum(reviews.values())

    print(f'You have performed {total_reviews} reviews on Stack Overflow as '
          f'of {last_updated}.')

    for queue, count in sorted(reviews.items(),
                               key=lambda x: x[1], reverse=True):
        print(f'{count}\t{queue}')


if __name__ == '__main__':
    main()
