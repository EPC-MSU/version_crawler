# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:43:47 2019

@author: zap
"""

import os
from tkinter import *
from tkinter import filedialog
import threading

# defaults hardcode definitions
default_exclusions = 'snapshot ДОКУМЕНТЫ download.ximc.ru bombardier'
default_path = 'z:\\'
default_log_filename_good = 'Crawl_results_good.txt'
default_log_filename_bad = 'Crawl_results_bad.txt'
default_regexp_good = '^([\w\d])+-(\d+\.\d+\.\d+)+(\.[a-z\d]{1,4})?(-[a-z\d\._]+)?(\.(zip|cod|json|txt|img|7z))?$'
default_regexp_bad = '^([A-Za-z_\d])+.?(\d+\.\d+\.\d+)(.[A-Za-z\d_]+)?(.[\(\)A-Za-z_\d-]+(\.([\d]+|x))?(\.([\d]+|x))?)?(-\([a-z_\d]+\))?'


class AddField:
    def __init__(self, wnd, row_num, field_label, default_text, file = False):
        self.lbl = Label(wnd, text=field_label)
        self.lbl.grid(column=0, row=row_num)
        self.txt = Entry(wnd, width=110)
        self.txt.grid(column=1, row=row_num)
        self.txt.configure()
        self.txt.insert(INSERT, default_text)
        if file:
            self.ofd = Button(wnd, text="Select file ...", command=self.ofd_click)
            self.ofd.grid(column = 2, row = row_num)
    def ofd_click(self):
        filename = filedialog.askopenfilename(title="Select file", filetypes=(("all files", "*.*"),))
        self.txt.delete(0, END)
        self.txt.insert(INSERT, filename)



window = Tk()
window.title('Version crawler')
window.geometry('900x200')
gui_exclusions = AddField(window, 0, 'Exclusions', default_exclusions)
gui_path = AddField(window, 1, 'Default path', default_path, True)
gui_log_filename_good = AddField(window, 2, 'Log filename', default_log_filename_good, True)
gui_regexp_good = AddField(window, 3, 'Correct regexp', default_regexp_good)
lbl = Label(window, text="Bad regexp allows to find close to correct names that do not comply with good regexp")
lbl.grid(column=1, row=4)
gui_log_filename_bad = AddField(window, 5, 'Log filename', default_log_filename_bad, True)
gui_regexp_bad = AddField(window, 6, 'Bad regexp', default_regexp_bad)


def Crawl(reg_exp_good, exclusions, root_dir, log_filename_good, reg_exp_bad, log_filename_bad):
    f_good = open(log_filename_good, 'w+')
    f_bad = open(log_filename_bad, 'w+')
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
        found_good = False
        found_bad = False

        CurrentDir = '\rFound in directory: {}\r\n'.format(dirName)
        for fname in fileList:
            if (reg_exp_bad.match(fname) != None) and (reg_exp_good.match(fname) == None):
                if (not found_bad):
                    f_bad.write('Found in directory: {}\n'.format(dirName))
                    found_bad = True
                    f_bad.flush()
                f_bad.write('\t{}\n'.format(fname))
            if (reg_exp_good.match(fname) != None):
                if (not found_good):
                    sys.stdout.write(CurrentDir)
                    f_good.write('Found in directory: {}\n'.format(dirName))
                    found_good = True
                    f_good.flush()
                sys.stdout.write('\t{}\r\n'.format(fname))
                f_good.write('\t{}\n'.format(fname))
    sys.stdout.write('\r ')  # To delete last string
    sys.stdout.flush()
    f_good.close()
    f_bad.close()


def clicked():
    regexp_good = re.compile(gui_regexp_good.txt.get())
    regexp_bad = re.compile(gui_regexp_bad.txt.get())
    exclusions = gui_exclusions.txt.get().split()
    root_dir = gui_path.txt.get()
    log_filename_good = gui_log_filename_good.txt.get()
    log_filename_bad = gui_log_filename_bad.txt.get()
    x = threading.Thread(target=Crawl, args=(regexp_good, exclusions, root_dir, log_filename_good, regexp_bad, log_filename_bad))
    x.daemon = True
    x.start()
    btn.config(state='disabled')


btn = Button(window, text="Start crawl", command=clicked)
btn.grid(column=0, row=7)
window.mainloop()
exit()
