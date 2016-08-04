#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *

def init_log(log_path):
    logging.config.fileConfig(log_path)
    main_logger = logging.getLogger('main')
    root_logger = logging.getLogger('root')
    return main_logger, root_logger


