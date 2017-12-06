#!/usr/bin/env python3

import exiftool
import glob
import operator
import timeit


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


def get_key(e):
    return e[1]


def entry2string(e):
    return '{:>6} : {:<4}'.format(e[0], e[1])


def main(path):
    fls = {}
    count = 0

    for f in glob.iglob(path, recursive=True):
        print(f)
        count += 1
        focal_length = get_exif(f)

        if focal_length in fls:
            fls[focal_length] += 1
        else:
            fls[focal_length] = 1

    print('Total files analyzed: {}'.format(count))
    print('Focal Lengths:')
    print("\n".join( map( entry2string, sorted(fls.items(), key=get_key, reverse=True)) ))


if __name__ == '__main__':

    #path = '/Users/mattmusc/Desktop/2017-Milano/*.dng'
    path = '/Volumes/Pictures/archivio/**/*.dng'

    timeit.Timer(main(path))

