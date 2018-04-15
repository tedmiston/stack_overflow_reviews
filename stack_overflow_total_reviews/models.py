from typing import NamedTuple


class ReviewQueue(NamedTuple):
    name: str
    slug: str

    @staticmethod
    def get_stats_url(slug):
        return f'https://stackoverflow.com/review/{slug}/stats'

    @staticmethod
    def get_review_url(slug):
        return f'https://stackoverflow.com/review/{slug}'
