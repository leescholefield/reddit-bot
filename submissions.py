"""
Filters submissions.
"""
from datetime import datetime


def filter_by_date(submissions, date):
    """
    Removes the submissions from the list made before the given date.

    :param submissions: list of submissions.
    :param date: date to remove before.
    :return: a list with the submissions made before a certain date removed.
    """
    if not isinstance(date, datetime):
        date = datetime.fromtimestamp(date)

    return [val for val in submissions
            if datetime.fromtimestamp(val.created)
            > date]


def filter_by_domain(submissions, domains):
    """
    Searches the submissions list and removes the one that contains a domain from the domain list.

    :param submissions: list of submissions
    :param domains:  list of domains.
    :return: a list with the submissions matching the domains removed.
    """

    return [val for val in submissions
            if val.domain not in domains]


def filter_selfposts(submissions):
    """
    Removes self-posts from the submissions list.

    :param submissions: list of submissions
    :return: a list with the self-post submissions removed
    """
    return None