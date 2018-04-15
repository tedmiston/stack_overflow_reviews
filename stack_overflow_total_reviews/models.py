from typing import NamedTuple


class ReviewQueue(NamedTuple):
    name: str
    slug: str

    def get_stats_url(self):
        return f'https://stackoverflow.com/review/{self.slug}/stats'

    def get_review_url(self):
        return f'https://stackoverflow.com/review/{self.slug}'


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
