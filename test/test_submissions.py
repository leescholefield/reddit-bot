from datetime import datetime, timedelta
import time
import unittest

from submissions import filter_by_date


class TestSubmission:
    def __init__(self, date):
        self.created = time.mktime(date.timetuple())


class SubmissionsTest(unittest.TestCase):

    def test_date_filter(self):
        date = datetime.today()
        sub1 = TestSubmission(date + timedelta(days=1))
        sub2 = TestSubmission(date - timedelta(hours=1))
        sub3 = TestSubmission(date - timedelta(minutes=10))

        all_list = [sub1, sub2, sub3]
        expected = [sub1]
        self.assertListEqual(expected, filter_by_date(all_list, date))
