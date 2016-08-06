#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
import util

main_ini = util.load_ini(MAIN_INI_PATH)

class Source:
    def __init__(self, _source):
        self.name = None
        self.root_linke = None
        self.keys = None
        self.api = None

        if 'name' in _source:
            self.name = _source['name']
        if 'root_link' in _source:
            self.root_link = _source['root_link']
        if 'keys' in _source:
            self.keys = _source['keys']
        if 'api' in _source:
            self.api = _source['api']


class MyHouse:
    def __init__(self):
        _sources = util.get_ini_value(main_ini, 'myhouse', 'sources', '')
        self.sources = []
        for _source in _sources.split(','):
            name = util.get_ini_value(main_ini, _source.strip(), 'name', '')
            root_link = util.get_ini_value(main_ini, _source.strip(), 'root_link', '')
            keys = util.get_ini_value(main_ini, _source.strip(), 'key', '')
            api = util.get_ini_value(main_ini, _source.strip(), 'api', '')
            source = Source({'name': name, 'root_link': root_link, 'keys': keys, 'api': api})
            self.sources.append(source)

