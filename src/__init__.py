#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import logging.config

log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'conf', 'log.ini')
import util
logger, root_logger = util.init_log(log_path)

