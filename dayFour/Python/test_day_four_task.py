from unittest import TestCase

import day_four_task

class TestSumOfTwoNumbers(TestCase):

    def test_that_sum_of_two_numbers_exists(self):
        day_four_task.sum_of_two_numbers([8, 6, 12, 4, -2], 6)

    def test_that_sum_of_two_numbers_returns_the_correct_value(self):
        actual = [8, -2]
        expected = day_four_task.sum_of_two_numbers([8, 6, 12, 4, -2], 6)
        self.assertEqual(actual, expected)

class TestRangeBetweenLargestAndSmallest(TestCase):

    def test_that_range_between_largest_and_smallest_returns_the_correct_value(self):
        day_four_task.range_between_largest_and_smallest_numbers([14, 9, 6, 5, 8, 10])

    def test_that_range_between_largest_and_smallest_returns_correct_value(self):
        actual = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        expected = day_four_task.range_between_largest_and_smallest_numbers([14, 9, 6, 5, 8, 10])
        self.assertEqual(actual, expected)
