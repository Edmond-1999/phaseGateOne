from unittest import TestCase

import facebook_like_system

class TestFacebookLikeSystem(TestCase):

    def test_that_the_likes_of_people_exists(self):
        facebook_like_system.the_likes_of_people(["Edmond"])

    def test_that_the_likes_of_people_gives_the_right_output_empty_list(self):
        actual = facebook_like_system.the_likes_of_people([])
        expected = "No one likes this"
        self.assertEqual(actual, expected)

    def test_that_the_likes_of_people_gives_the_right_output_one_name(self):
        actual = facebook_like_system.the_likes_of_people(["Edmond"])
        expected = "Edmond likes this"
        self.assertEqual(actual, expected)

    def test_that_the_likes_of_people_gives_the_right_output_two_names(self):
        actual = facebook_like_system.the_likes_of_people(["Edmond", "Peter"])
        expected = "Edmond and Peter like this"
        self.assertEqual(actual, expected)

    def test_that_the_likes_of_people_gives_the_right_output_three_names(self):
        actual = facebook_like_system.the_likes_of_people(["Edmond", "Peter", "Alex"])
        expected = "Edmond, Peter and Alex like this"
        self.assertEqual(actual, expected)

    def test_that_the_likes_of_people_gives_the_right_output_more_than_three_names(self):
        actual = facebook_like_system.the_likes_of_people(["Edmond", "Peter", "Alex", "John", "Mark"])
        expected = "Edmond, Peter and 3 other(s) like this"
        self.assertEqual(actual, expected)

