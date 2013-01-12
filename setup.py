#!/usr/bin/env python
# encoding: utf-8

import re
from os import *
from os.path import *

def main():
    basedir, homedir = join(getcwd(), dirname(__file__)), getenv('HOME')
    for x in listdir(basedir):
        if re.match(r'.*\.swp$|^\..*|.*~$|^setup\.py$', x):
            continue
        src = join(basedir, x)
        target = join(homedir, re.sub(r'^_', '.', x))
        print '%s -> %s' % (src, target)
        try:
            symlink(src, target)
        except OSError, ex:
            print str(ex)

if __name__ == '__main__':
    main()
