#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __base__ import *
from myhouse import *

class TestCase(unittest.TestCase):
    def test_welcome(self):
        self.assertTrue(True)

    def test_MyHouse(self):
        myhouse = MyHouse()
        self.assertTrue(myhouse)
        self.assertTrue(myhouse.sources)
        self.assertTrue(len(myhouse.sources) > 0)
        for source in myhouse.sources:
            self.assertTrue(source.name)

unittest.main()
