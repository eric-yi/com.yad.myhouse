#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __base__ import *
import spider
from house import HousePage

class TestCase(unittest.TestCase):
    def test_welcome(self):
        self.assertTrue(True)

    def test_get_shanghai_phonix(self):
        url = 'http://esf.sh.fang.com/house/g22-kw%ba%c3%ca%c0%b7%ef%bb%cb%b3%c7'
        module = 'soufan'
        root_link = 'http://esf.sh.fang.com'
        house_page = spider.get(url, module, root_link)
        self.assertIsNotNone(house_page)
        self.assertTrue(len(house_page.houses) > 0)

    def test_get(self):
        url = 'http://esf.sh.fang.com/house/g22-j280-k2100-l3010-kw%c3%fb%b6%bc%d0%c2%b3%c7'
        module = 'soufan'
        root_link = 'http://esf.sh.fang.com'
        result = spider.get(url, module, root_link)
        self.assertIsNotNone(result)

    def test_extract(self):
        url = 'http://esf.sh.fang.com/house/g22-j280-k2100-l3010-kw%c3%fb%b6%bc%d0%c2%b3%c7'
        header, html = spider.connect(url)
        house_page = spider.extract(html, 'soufan')
        self.assertTrue(house_page)

unittest.main()

