#!/usr/bin/env python
# encoding: utf-8

import re
from os import *
from os.path import *

def main():
    basedir, homedir = join(getcwd(), dirname(__file__)), getenv('HOME')
    for x in [join(basedir, x) for x in listdir('.')]:
        if re.match(r'.*\.swp$|^\..*|.*~$|^setup\.py$', x):
            continue
        target = join(homedir, re.sub(r'^_', '.', basename(x)))
        print '%s -> %s' % (x, target)
        symlink(x, target)

if __name__ == '__main__':
    main()
