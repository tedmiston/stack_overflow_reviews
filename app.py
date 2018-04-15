"""
Keep track of the number of reviews I've done on Stack Overflow.
"""


def get_review_queue_stats_url(queue_name):
    return f'https://stackoverflow.com/review/{queue_name}/stats'


def get_reviews_all_time():
    total_reviews = {
        'suggested-edits': 6,
        'triage': 293,
        'helper': 0,
        'low-quality-posts': 0,
        'late-answers': 8,
        'first-posts': 21,
    }
    last_updated = '2018-04-14'
    return total_reviews, last_updated


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
