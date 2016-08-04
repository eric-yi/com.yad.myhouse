#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __base__ import *
import spider

class TestCase(unittest.TestCase):
    def test_welcome(self):
        self.assertTrue(True)

    def test_grab(self):
        # test for fetch
        url = 'http://esf.sh.fang.com/house/g22-j280-k2100-l3010-kw%c3%fb%b6%bc%d0%c2%b3%c7'
        header, html = spider.get(url)
        self.assertTrue(header is not None)
        self.assertTrue(html is not None)
        self.assertTrue('content-type' in header)
        self.assertTrue('html' in html)
        # test for extract
        spider.extract(html, 'soufan')


unittest.main()
