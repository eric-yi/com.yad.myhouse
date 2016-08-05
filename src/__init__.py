#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import logging.config

# constants
INI_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ini')
LOG_INI_PATH = os.path.join(INI_PATH, 'log.ini')
MAIN_INI_PATH = os.path.join(INI_PATH, 'myhouse.ini')

import util
logger, root_logger = util.init_log(LOG_INI_PATH)
