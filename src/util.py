#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
import ConfigParser
from datetime import datetime
import codecs

def init_log(log_path):
    logging.config.fileConfig(log_path)
    main_logger = logging.getLogger('main')
    root_logger = logging.getLogger('root')
    return main_logger, root_logger

def load_ini(ini_path):
    ini = ConfigParser.ConfigParser()
    ini.read(ini_path)
    return ini

def get_ini_value(ini, option, key, default):
    try:
        if isinstance(default, int):
            value = ini.getint(option, key)
        else:
            value = ini.get(option, key)
        if value is None:
            return default
        else:
            return value
    except:
        pass
    return default

def current_time_str():
    return datetime.now().strftime('%Y%m%d%H%M%S')

def write_store(filename, contents):
    filepath = os.path.join(STORE_PATH, filename)
    with codecs.open(filepath, 'w', 'utf-8') as file:
        file.write(contents)
        file.close()


