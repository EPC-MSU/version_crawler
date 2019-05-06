# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:43:47 2019

@author: zap
"""

import os
import re
import sys

release = re.compile('^([\w\d])+-(\d+\.\d+\.\d+)+(\.[a-z\d]{1,4})?(-[a-z\d\._]+)?(\.(zip|cod|json|txt|img|7z))?$')
exclusions = ['snapshot', 'ДОКУМЕНТЫ', 'download.ximc.ru', 'bombardier']

RootDir = 'z:\\'
Found = False
f = open("Crawl_results.txt", "w+")
for dirName, subdirList, fileList in os.walk(RootDir,
                                             topdown=True):  # topdown must be true for exclusion subdirs to work
    # Filtering bad dirs
    for index, subdir in enumerate(subdirList):
        for ex in exclusions:
            if (ex in subdir):
                subdirList.remove(subdir)
    if (not Found):
        sys.stdout.write("\rScanning directory {}".format(dirName))
    else:
        sys.stdout.write("Scanning directory {}".format(dirName))
    sys.stdout.flush()
    Found = False

    CurrentDir = '\rFound in directory: {}\r\n'.format(dirName)
    for fname in fileList:
        if (release.match(fname) != None):
            if (not Found):
                sys.stdout.write(CurrentDir)
                f.write('Found in directory: {}\n'.format(dirName))
                Found = True
                f.flush()
            sys.stdout.write('\t{}\r\n'.format(fname))
            f.write('\t{}\n'.format(fname))
sys.stdout.write('\r ')  # To delete last string
sys.stdout.flush()
f.close()
