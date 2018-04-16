from typing import NamedTuple

from . import conf
from .cache import cache


def fetch_reputation():
    return 2031


class User(NamedTuple):
    id: int

    @property
    def reputation(self):
        return int(cache.get_or_update('reputation', fetch_reputation,
                                       ttl=conf.CACHE_TTL_REPUTATION))


class ReviewQueue(NamedTuple):
    name: str
    slug: str
    reputation: int  # threshold for accessing this queue

    def _get_url(self, suffix):
        BASE = 'https://stackoverflow.com/review'
        return BASE + suffix

    def get_stats_url(self):
        return self._get_url(f'/{self.slug}/stats')

    def get_review_url(self):
        return self._get_url(f'/{self.slug}')


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
