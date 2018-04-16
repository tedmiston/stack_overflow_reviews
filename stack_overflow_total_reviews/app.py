"""
Keep track of the number of reviews I've done on Stack Overflow.
"""

from . import conf
from .models import User
from .stats import get_reviews_all_time
from .status import get_review_queues_current_status


def main():
    user = User(conf.STACK_OVERFLOW_USER_ID)

    reviews, last_updated = get_reviews_all_time()

    total_reviews = sum(reviews.values())

    print(f'You\'ve performed {total_reviews} reviews as of {last_updated}:')
    for queue, count in sorted(reviews.items(),
                               key=lambda x: x[1], reverse=True):
        url = queue.get_stats_url()
        print(f'{count}\t{queue.name} ({url})')

    print()
    print('Current queue status:')
    for queue, count in sorted(get_review_queues_current_status(user).items(),
                               key=lambda x: x[1], reverse=True):
        url = queue.get_review_url()
        print(f'{count}\t{queue.name} ({url})')


if __name__ == '__main__':
    main()
