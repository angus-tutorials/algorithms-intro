import json
import unittest

from surveys.your_solution import find_fake_surveys


def are_lists_equal_regardless_of_order(list1, list2):
    """
    Little helper function to compare lists
    """
    set1 = set(frozenset(item) for item in list1)
    set2 = set(frozenset(item) for item in list2)
    return set1 == set2


class TestFindFakeSurveys(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        with open("data/surveys_small.json") as file:
            cls.small = json.load(file)
            cls.small_expected = [(123, 789)]

        with open("data/surveys_medium.json") as file:
            cls.medium = json.load(file)
            cls.medium_expected = [(123, 456), (789, 1011)]

        with open("data/surveys_large.json") as file:
            cls.large = json.load(file)
            cls.large_expected = [(123, 456), (789, 1011), (121314, 151617)]

        with open("data/surveys_xl.json") as file:
            cls.xl = json.load(file)
            cls.xl_expected = [(123, 456), (789, 1011), (121314, 151617)]

    def test_empty(self):
        actual = find_fake_surveys([])
        expected = []
        self.assertTrue(are_lists_equal_regardless_of_order(expected, actual))

    def test_with_no_fake_surveys(self):
        surveys = [
            {
                "tx_id": 123,
                "name": "hello"
            },
        ]
        actual = find_fake_surveys(surveys)
        expected = []
        self.assertTrue(are_lists_equal_regardless_of_order(expected, actual))

    def test_small(self):
        actual = find_fake_surveys(self.small)
        expected = self.small_expected
        self.assertTrue(are_lists_equal_regardless_of_order(expected, actual))

    def test_medium(self):
        actual = find_fake_surveys(self.medium)
        expected = self.medium_expected
        self.assertTrue(are_lists_equal_regardless_of_order(expected, actual))

    def test_large(self):
        actual = find_fake_surveys(self.large)
        expected = self.large_expected
        self.assertTrue(are_lists_equal_regardless_of_order(expected, actual))

    def test_xl(self):
        actual = find_fake_surveys(self.xl)
        expected = self.xl_expected
        self.assertTrue(are_lists_equal_regardless_of_order(expected, actual))


if __name__ == '__main__':
    unittest.main()
