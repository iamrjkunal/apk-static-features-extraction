#!/usr/bin/env python
# -*- coding: utf-8 -*-

import androlyze, argparse, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    cannot_analyze = []
    print os.path.basename(os.path.normpath(directory))
    for filename in os.listdir(directory):
        if (os.path.splitext(filename)[1] == '.apk') or (os.path.splitext(filename)[1] == '.vir'):
            try:
                print 'Analyzing', filename
                a,d,dx = androlyze.AnalyzeAPK(os.path.join(directory, filename), decompiler='dad')
                androlyze.save_session([a,d,dx], os.path.join(directory, filename+'.json'))
            except Exception, e:
                print "Exception in user code:"
                print '-'*60
                traceback.print_exc(file=sys.stdout)
                print '-'*60
                cannot_analyze.append(filename)
                continue

    print 'Cannot analyze:'
    cannot = open(os.path.join(directory, 'cannot_analyze.txt'), 'w')
    cannot.write('Cannot analyze:\n')
    for filename in cannot_analyze:
        print filename
        cannot.write(filename + '\n')
    cannot.close()

if __name__ == '__main__':
    main()