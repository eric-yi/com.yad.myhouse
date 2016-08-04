#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
import httplib2
import importlib

http = httplib2.Http()

def grab(url):
    pass

def get(url):
    response, html = http.request(url, method='GET')
    header = response.dict
    content_type = header['content-type']
    lang_code = content_type[content_type.index('charset=')+len('charset='):]
    return header, html.decode(lang_code, 'ignore')

def extract(html, module):
    extract_name = 'extract_' + module + '.py'
    extract_proxy = importlib.import_module(extract_name)
    extract_proxy.extract(html)


