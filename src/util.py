#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
import ConfigParser

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

