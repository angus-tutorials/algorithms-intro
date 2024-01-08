import json
import unittest

from meetings.your_solution import time_spent_in_meetings


class TestCalendar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        with open("data/meetings_xs.json") as file:
            cls.xs = json.load(file)
            # [(2, 3), (2.5, 4), (5, 6), (6, 7)]
            # 4 hours. which is 240 minutes
            cls.xs_expected = 240

        with open("data/meetings_small.json") as file:
            cls.small = json.load(file)
            cls.small_expected = 330

    def test_solution_xs(self):
        actual = time_spent_in_meetings(self.xs)
        self.assertEqual(self.xs_expected, actual)

    def test_solution_small(self):
        actual = time_spent_in_meetings(self.small)
        self.assertEqual(self.small_expected, actual)


if __name__ == '__main__':
    unittest.main()
