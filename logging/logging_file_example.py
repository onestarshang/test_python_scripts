#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""Example use of Python's logging module writing to a file.

See http://blog.doughellmann.com/2007/05/pymotw-logging.html
"""

__module_id__ = "$Id$"
#end_pymotw_header

import logging
from logging.config import fileConfig

# print dir(fileConfig)

fileConfig('logging.cfg')
logger1 = logging.getLogger('test1')
logger2 = logging.getLogger('test2')

logging.info('test root.....')

"""
logformat = '%(asctime)s [%(name)s] %(levelname)s %(filename)s --> %(funcName)s: %(message)s'

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=logformat,
                    )

logging.debug('This message should go to the log file')

logger1 = logging.getLogger("logging.test1")
logger2 = logging.getLogger("logging.test2")

f = open(LOG_FILENAME, 'rt')
try:
    body = f.read()
finally:
    f.close()

print 'FILE:'
print body
"""

def test1():
	logger1.debug('ddd')

def test2():
	logger2.warning('test2 --------- ')

test1()
test2()


logger1.info('info ---- ')