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
        for house in houses:
            #self.assertEquals('名都新城', house.name)
            self.assertIsNotNone(house.name)
            self.assertIsNotNone(house.village_name)
            self.assertIsNotNone(house.storey)
            self.assertTrue(house.orientation != -1)
            self.assertTrue(house.age != -1)
            self.assertTrue(house.age > 1990)
            self.assertTrue(house.building != -1)
            self.assertIsNotNone(house.address)
            self.assertIsNotNone(house.agent)
            self.assertIsNotNone(house.policy)
            self.assertTrue(house.total_price != -1)
            self.assertTrue(house.total_price > 1000000)
            self.assertTrue(house.centiare_price != -1)
            self.assertTrue(house.centiare_price > 1000)


unittest.main()
