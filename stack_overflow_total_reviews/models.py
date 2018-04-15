from typing import NamedTuple


class ReviewQueue(NamedTuple):
    name: str
    slug: str
    reputation: int  # threshold for accessing this queue

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
        ReviewQueue('Close Votes', 'close', 3000),
        ReviewQueue('First Posts', 'first-posts', 500),
        ReviewQueue('Help and Improvement', 'helper', 2000),
        ReviewQueue('Late Answers', 'late-answers', 500),
        ReviewQueue('Low Quality Posts', 'low-quality-posts', 2000),
        ReviewQueue('Reopen Votes', 'reopen', 3000),
        ReviewQueue('Suggested Edits', 'suggested-edits', 2000),
        ReviewQueue('Triage', 'triage', 500),
    )
