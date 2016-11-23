#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess

directory = '/Users/liuchushu/Downloads/Dataset/vir-dataset'
def main():
    for subdirectory in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, subdirectory)):
            r = subprocess.call(['python', 'get_apk_features.py', '-d', os.path.join(directory, subdirectory), '-s', '-1'])

if __name__ == '__main__':
    main()