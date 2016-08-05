#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __base__ import *
import util

class TestCase(unittest.TestCase):
    def test_welcome(self):
        self.assertTrue(True)

    def test_load_ini(self):
        main_ini = util.load_ini(MAIN_INI_PATH)
        self.assertIsNotNone(main_ini)

    def test_get_ini_value(self):
        main_ini = util.load_ini(MAIN_INI_PATH)
        _value = util.get_ini_value(main_ini, 'myhouse', 'sources', None)
        _value = util.get_ini_value(main_ini, 'soufun', 'api-prefix', None)
        self.assertIsNotNone(_value)

unittest.main()
