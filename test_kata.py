#!/usr/bin/python
# -*- coding: utf-8 -*-

from scalc import string_add
import unittest
from io import StringIO
import sys
import os

class StringAddTests(unittest.TestCase):
    
    def test_zero_when_empty_string(self):
        assert string_add('') == 0, 'BASIC TEST PASSED'

    def test_one_number(self):
        assert string_add('1') == 1, 'TEST A PASSED'

    def test_two_numbers(self):
        assert string_add('1,2') == 3

    def test_three_numbers(self):
        assert string_add('1,2,4') == 7

    def test_three_big_numbers(self):
        assert string_add('11,124,414') == 549

    def test_throw_exception_when_negative_numbers_included(self):
       with self.assertRaisesRegex(ValueError, 'no negatives allowed: -1'):
          string_add('-1,0,1')

    def test_throw_exception_when_multiple_negative_numbers_included(self):
        with self.assertRaisesRegex(ValueError, 'no negatives allowed: -1 -1 -2'):
            string_add('-1,0,-1,-2')

    def test_expected_result_with_new_line(self):
        assert string_add('1\n2,3') == 6

    def test_return_sum_with_semi_colon_delimiter(self):
        assert string_add('//;\n1;2') == 3

    def test_ignore_numbers_over_1000(self):
        assert string_add('1,2,1001') == 3

    def test_expected_sum_delimiter_any_length(self):
        assert string_add('//[***]\n1***2***3') == 6

    def test_return_6_with_multiple_delimiters(self):
        assert string_add('//[*][%]\n1*2%3') == 6

    def test_return_6_with_std_out(self):
        try:
            saved_stdout = sys.stdout
            out = StringIO()
            sys.stdout = out
            string_add('1,2,3', out=out)
            output = out.getvalue().strip()
            assert output == '6'
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()


            
