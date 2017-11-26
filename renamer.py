#!/usr/bin/env python3

if __name__ == '__main__':

    import os
    import sys

    if len(sys.argv) < 2:
        print('./renamer.py <directory>')
        sys.exit(1)

    path = sys.argv[1]
    for fname in os.listdir(path):

        old_name = os.path.join(path, fname)
        new_name = os.path.join(path, fname[1:])

        os.rename(old_name, new_name)
