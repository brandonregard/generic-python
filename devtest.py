import string

from datetime import datetime, timedelta


class Solutions(object):

    def greater_than_avg(self, nums):
        """Given a list of numbers, return a list containing any numbers that
        are greater than the average of the original list.
        """
        return [n for n in nums if n > sum(nums) / len(nums)]

    def sort_fruit(self, fruit):
        """Given a list of dictionaries with a count key, return the same list
        of dictionaries sorted by the count key.
        """
        return sorted(fruit, key=lambda k: k['count'])

    def transpose_dict(self, d):
        """Return a transposed version of dictionary d."""
        return {v: k for k, v in d.items()}

    def week_start_end(self, d):
        """Given a date, return a tuple with the start of the week and the end
        of the week.
        """
        return (
            (d - timedelta(days=d.weekday())).replace(
                hour=0, minute=0, second=0, microsecond=0)
        ,
            (d + timedelta(days=6-d.weekday())).replace(
                hour=23, minute=59, second=59, microsecond=999999)
        )

    def month_last_day(self, d):
        """Given a date, return the number of days in the month."""
        return (d.replace(month=d.month%12+1, day=1) - timedelta(days=1)).day

    def palindrome_test_function(self):
        """Return a function object that will accept 1 argument and can be
        called to check for palindromes.
        """
        return lambda s: (s.lower().translate(
            None, ' %s' % string.punctuation) ==
            ''.join(reversed(s)).lower().translate(
                None, ' %s' % string.punctuation))

    def string_parse(self, s):
        """Given a custom table as a string, return a list row of tuples."""
        result = []
        like = dislike = ''
        for l in s.splitlines()[3:-1]:
            p = l[1:-1].partition('|')
            if p[1] != '|':
                result.append((like, dislike))
                like = dislike = ''
            else:
                like = ('%s%s' % (like, p[0])).strip()
                dislike = ('%s%s' % (dislike, p[2])).strip()
        return result[1:]
