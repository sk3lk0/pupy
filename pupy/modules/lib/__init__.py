# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime

import sys


def size_human_readable(num, suffix=''):
    try:
        num = int(num)
        for unit in [suffix or 'B','K','M','G','T','P','E','Z']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)
    except:
        return '0.0B'


def file_timestamp(timestamp, time=False):
    try:
        d = datetime.fromtimestamp(timestamp)
        if time:
            return str(d.strftime('%d/%m/%y %H:%M:%S'))
        else:
            return str(d.strftime('%d/%m/%y'))
    except:
        return '00/00/00'
