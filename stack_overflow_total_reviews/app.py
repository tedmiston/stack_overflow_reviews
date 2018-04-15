"""
Keep track of the number of reviews I've done on Stack Overflow.
"""

from .stats import get_reviews_all_time
from .status import get_review_queues_current_status


def main():
    reviews, last_updated = get_reviews_all_time()

    total_reviews = sum(reviews.values())

    print(f'You have performed {total_reviews} reviews on Stack Overflow as '
          f'of {last_updated}.')

    for queue, count in sorted(reviews.items(),
                               key=lambda x: x[1], reverse=True):
        url = queue.get_stats_url()
        print(f'{count}\t{queue.name} ({url})')

    print()
    print('-- Current queue status --')
    for queue, count in get_review_queues_current_status().items():
        url = queue.get_review_url()
        print(f'{count}\t{queue.name} ({url})')


if __name__ == '__main__':
    main()
