from datetime import datetime, timedelta
import time
import unittest

from filter import *


class TestSubmission:
    def __init__(self, date=None, domain=None):
        if date is not None:
            self.created_utc = time.mktime(date.timetuple())
        self.domain = domain


class FilterTest(unittest.TestCase):

    def test_filter_by_invalid(self):
        """ Tests that an invalid filter_by call throws an exception"""
        self.assertRaises(ValueError, filter_by, [], 'domain')

    def test_date_filter(self):
        date = datetime.today()
        sub1 = TestSubmission(date + timedelta(days=1), '')
        sub2 = TestSubmission(date - timedelta(hours=1), '')
        sub3 = TestSubmission(date - timedelta(minutes=10), '')

        all_list = [sub1, sub2, sub3]
        expected = [sub1]
        self.assertListEqual(expected, filter_by_date(all_list, date))

    def test_domain_filter(self):
        banned_domains = ['youtube.com', 'facebook.com']

        sub1 = TestSubmission(domain='youtube.com')
        sub2 = TestSubmission(domain='other.com')
        sub3 = TestSubmission(domain='facebook.com')
        all_list = [sub1, sub2, sub3]
        expected = [sub2]

        self.assertListEqual(expected, filter_by_domain(all_list, banned_domains))

    def test_remove_selfposts(self):
        sub1 = TestSubmission(domain='self.java')
        sub2 = TestSubmission(domain='youtube.com')
        sub3 = TestSubmission(domain='self.python')
        all_list = [sub1, sub2, sub3]
        expected = [sub2]

        self.assertListEqual(expected, filter_selfposts(all_list))
