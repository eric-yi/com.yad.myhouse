#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __base__ import *
import spider
from house import HousePage
from myhouse import Source

class TestCase(unittest.TestCase):
    def test_welcome(self):
        self.assertTrue(True)

    @unittest.skip('skip test')
    def test_get_shanghai_phoenix(self):
        url = 'http://esf.sh.fang.com/house/g22-kw%ba%c3%ca%c0%b7%ef%bb%cb%b3%c7'
        module = 'soufun'
        root_link = 'http://esf.sh.fang.com'
        house_page = spider.get(url, module, root_link)
        self.assertIsNotNone(house_page)
        self.assertTrue(len(house_page.houses) > 0)

    @unittest.skip('skip test')
    def test_get(self):
        url = 'http://esf.sh.fang.com/house/g22-j280-k2100-l3010-kw%c3%fb%b6%bc%d0%c2%b3%c7'
        module = 'soufun'
        root_link = 'http://esf.sh.fang.com'
        result = spider.get(url, module, root_link)
        self.assertIsNotNone(result)

    @unittest.skip('skip test')
    def test_extract(self):
        url = 'http://esf.sh.fang.com/house/g22-j280-k2100-l3010-kw%c3%fb%b6%bc%d0%c2%b3%c7'
        header, html = spider.connect(url)
        house_page = spider.extract(html, 'soufun')
        self.assertTrue(house_page)

    @unittest.skip('skip test')
    def test_get_and_write(self):
        source = Source({
            'name': 'soufun-mingdu',
            'module': 'soufun',
            'root_link': 'http://esf.sh.fang.com',
            'keys': '名都新城,二居,80-100平米',
            'api': 'http://esf.sh.fang.com/house/g22-j280-k2100-l3010-kw%c3%fb%b6%bc%d0%c2%b3%c7'
        })
        spider.get_and_write(source)
        self.assertTrue(True)

    #@unittest.skip('skip test')
    def test_grab(self):
        spider.grab()
        self.assertTrue(True)

unittest.main()

