#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __base__ import *
import util

LOG_PATH = '../conf/log.ini'

class TestCase(unittest.TestCase):
    def test_welcome(self):
        self.assertTrue(True)

    def test_init_log(self):
        logger.info('test')
        self.assertTrue(True)

unittest.main()
