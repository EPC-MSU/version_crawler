# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:43:47 2019

@author: zap
"""

import os
from tkinter import *

# defaults hardcode definitions
default_exclusions = 'snapshot ДОКУМЕНТЫ download.ximc.ru bombardier'
default_path = 'z:\\'
default_log_filename = 'Crawl_results.txt'
default_regexp = '^([\w\d])+-(\d+\.\d+\.\d+)+(\.[a-z\d]{1,4})?(-[a-z\d\._]+)?(\.(zip|cod|json|txt|img|7z))?$'


class AddField:
    def __init__(self, wnd, row_num, field_label, default_text):
        self.lbl = Label(wnd, text=field_label)
        self.lbl.grid(column=0, row=row_num)
        self.txt = Entry(wnd, width=100)
        self.txt.grid(column=1, row=row_num)
        self.txt.configure()
        self.txt.insert(INSERT, default_text)


window = Tk()
window.title('Version crawler')
window.geometry('750x200')
gui_exclusions = AddField(window, 0, 'Exclusions', default_exclusions)
gui_path = AddField(window, 1, 'Default path', default_path)
gui_log_filename = AddField(window, 2, 'Log filename', default_log_filename)
gui_regexp = AddField(window, 3, 'Regular expression', default_regexp)


def clicked():
    release = re.compile(gui_regexp.txt.get())
    exclusions = gui_exclusions.txt.get().split()
    root_dir = gui_path.txt.get()
    log_filename = gui_log_filename.txt.get()
    f = open(log_filename, 'w+')
    found = False
    for dirName, subdirList, fileList in os.walk(root_dir,
                                                 topdown=True):  # topdown must be true for exclusion subdirs to work
        # Filtering bad dirs
        for index, subdir in enumerate(subdirList):
            for ex in exclusions:
                if ex in subdir:
                    subdirList.remove(subdir)
        if not found:
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


btn = Button(window, text="Start crawl", command=clicked)
btn.grid(column=0, row=4)
window.mainloop()
