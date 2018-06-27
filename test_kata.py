#!/usr/bin/python
# -*- coding: utf-8 -*-

from kata import string_add
import unittest


class StringAddTests(unittest.TestCase):

    def test_empty_string(self):
        assert string_add('') == 0, 'BASIC TEST PASSED'

    def test_one_number(self):
        assert string_add('1') == 1, 'TEST A PASSED'

    def test_two_numbers(self):
        assert string_add('1,2') == 3

    def test_three_numbers(self):
        assert string_add('1,2,4') == 7

    def test_three_big_numbers(self):
        assert string_add('11,124,414') == 549

    def test_negative(self):
        assert string_add('-1,1,0') == 0

    def test_new_line(self):
        assert string_add('1\n2,3') == 6

    def test_return_sum_with_semi_colon_delimiter(self):
        assert string_add('//;\n1;2') == 3

        


if __name__ == '__main__':
    unittest.main()


            