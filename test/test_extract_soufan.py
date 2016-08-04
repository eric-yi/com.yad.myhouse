#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __base__ import *
import spider, extract_soufan

class TestCase(unittest.TestCase):
    def test_welcome(self):
        self.assertTrue(True)

    def test_extract_first_page(self):
        url = 'http://esf.sh.fang.com/house/g22-j280-k2100-l3010-kw%c3%fb%b6%bc%d0%c2%b3%c7'
        _, html = spider.get(url)
        # test for extract
        total, houses = extract_soufan.extract_first_page(html)
        self.assertIsNotNone(total)
        self.assertIsNotNone(houses)
        self.assertTrue(int(total) > 0)
        self.assertTrue(len(houses) > 0)



unittest.main()
