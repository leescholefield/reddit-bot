"""
Filters submissions.
"""
from datetime import datetime
import re


def filter_by(submissions, *args, **kwargs):
    """
    Utility function. Filters the submissions list by the methods provided in args.

    :param submissions: submission list to filter
    :param args: methods to filter it by. Either 'date', 'domain' or 'self-posts'
    :param kwargs: additional data required for desired filtering methods.
    :return: a list of filtered submissions.
    """
    for val in args:
        if val == 'self-posts':
            submissions = filter_selfposts(submissions)
        elif val == 'domain':
            submissions = filter_by_domain(submissions, kwargs['domain'])
        elif val == 'date':
            submissions = filter_by_date(submissions, kwargs['date'])
        else:
            raise ValueError(val, ' is not recognized as a valid param')

    return submissions


def filter_by_date(submissions, date):
    """
    Removes the submissions from the list made before the given date.

    :param submissions: list of submissions.
    :param date: date to remove before.
    :return: a list with the submissions made before a certain date removed.
    """
    if not isinstance(date, datetime):
        date = datetime.utcfromtimestamp(date)

    return [val for val in submissions
            if datetime.utcfromtimestamp(val.created_utc)
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
    regex = re.compile('self.*')

    return [val for val in submissions
            if re.search(regex, val.domain) is None]
