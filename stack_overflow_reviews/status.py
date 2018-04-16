import json
from collections import OrderedDict

from requests_html import HTMLSession

from . import conf
from .cache import cache
from .models import get_queues


def fetch_counts():
    session = HTMLSession()
    r = session.get('https://stackoverflow.com/review')

    counts = {}
    for queue_row in r.html.find('.dashboard-item'):
        queue_title = queue_row.find('.dashboard-title', first=True).text
        if queue_title == 'Meta Reviews':
            continue

        queue_more = queue_row.find('.dashboard-activity-more', first=True)
        recent_reviews_url = queue_more.attrs['href']
        queue_slug = (recent_reviews_url
                      .replace('/review/', '')
                      .replace('/stats', ''))

        dashboard_num = queue_row.find('.dashboard-num', first=True)
        num_exact = dashboard_num.attrs['title']
        num_exact = int(num_exact.replace(',', ''))
        # num_short = dashboard_num.text
        # units = queue_row.find('.dashboard-unit', first=True).text

        # print(queue_title, queue_slug, num_short, num_exact, units)

        counts[queue_slug] = num_exact

    counts_json = json.dumps(counts)

    return counts_json


def get_review_queues_current_status(user=None):
    """
    Which queues have questions/answers/posts/edits available for review?

    https://stackoverflow.com/review
    """

    # only include queues accessible at this user's reputation level
    user_reputation = user.reputation
    queues = get_queues()
    if user is not None:
        queues = (x for x in queues if x.reputation <= user_reputation)

    counts = cache.get_or_update('status', fetch_counts,
                                 ttl=conf.CACHE_TTL_QUEUE_STATUS)
    counts = json.loads(counts)

    queue_counts = OrderedDict([
        (queue, counts.get(queue.slug, 0)) for queue in queues])
    return queue_counts
