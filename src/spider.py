#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
import httplib2
import importlib
import threading
import json
from myhouse import myhouse
import util

http = httplib2.Http()

def grab():
    for source in myhouse.sources:
        thread = threading.Thread(target=get_and_write, args=(source,))
        thread.start()

def get_and_write(source):
    now = util.current_time_str()
    server_page = get(source.api, source.module, source.root_link)
    #logger.debug(server_page.to_dict())
    server_page_json = json.dumps(server_page.to_dict(), encoding="UTF-8", ensure_ascii=False)
    filename = '%s-%s.json' % (source.name, now)
    util.write_store(filename, server_page_json)

def get(url, module, root_link):
    logger.debug('get url: %s' % (url))
    n = 0
    _, html = connect(url)
    server_page = extract(html, module)
    total = server_page.total - 1
    url = root_link + server_page.next_link
    while n < total:
        logger.debug('get url: ' + url)
        _, html = connect(url)
        _server_page = extract(html, module)
        server_page.houses.extend(_server_page.houses)
        if not _server_page.next_link:
            break
        url = root_link + _server_page.next_link
        n = n + 1
    return server_page

def connect(url):
    #response, html = http.request(url, method='GET')
    response, html = httplib2.Http().request(url, method='GET')
    header = response.dict
    content_type = header['content-type']
    lang_code = content_type[content_type.index('charset=')+len('charset='):]
    return header, html.decode(lang_code, 'ignore')

def extract(html, module):
    extract_name = 'extract_' + module
    extract_proxy = importlib.import_module(extract_name)
    return extract_proxy.extract(html)

