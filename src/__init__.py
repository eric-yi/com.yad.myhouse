#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import io
import logging.config

# constants
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE_PATH = os.path.join(ROOT_PATH, 'stores')
INI_PATH = os.path.join(ROOT_PATH, 'ini')
LOG_INI_PATH = os.path.join(INI_PATH, 'log.ini')
MAIN_INI_PATH = os.path.join(INI_PATH, 'myhouse.ini')

import util
logger, root_logger = util.init_log(LOG_INI_PATH)
