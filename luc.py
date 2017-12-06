#!/usr/bin/env python3

import exiftool
import glob
import operator


def get_exif(fname):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(fname)
        return metadata['EXIF:FocalLength']
    return 0


def build_histogram(focal_lengths):
    fls = {}
    for focal_length in focal_lengths:
        if focal_length in fls:
            fls[focal_length] += 1
        else:
            fls[focal_length] = 1
    return fls


def get_key(key):
    return key


def entry2string(e):
    return '{:>6} : {:<4}'.format(e[0], e[1])

if __name__ == '__main__':

    fls = {}
    path = '/Users/mattmusc/Desktop/2017-Milano/*.dng'
    count = 0

    for f in glob.iglob(path, recursive=True):
        count += 1
        focal_length = get_exif(f)

        if focal_length in fls:
            fls[focal_length] += 1
        else:
            fls[focal_length] = 1

    print('Total files analyzed: {}'.format(count))
    print('Focal Lengths:')
    print("\n".join( map( entry2string, fls.items() ) ))
