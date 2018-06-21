#!/usr/bin/python
# -*- coding: utf-8 -*-

from kata import string_add
import unittest


class StringAddTests(unittest.TestCase):

    def testBasic(self):
        assert string_add('') == 0, 'BASIC TEST PASSED'

    def testA(self):
        assert string_add('1') == 1, 'TEST A PASSED'

    def testB(self):
        assert string_add('1,2') == 3

    def testC(self):
        assert string_add('1,2,4') == 7

    def testD(self):
        assert string_add('11,124,414') == 549

    def testE(self):
        assert string_add('-1,1,0') == 0

    def test_new_line(self):
        assert string_add('1\n2,3') == 6


if __name__ == '__main__':
    unittest.main()


            