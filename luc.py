#!/usr/bin/env python3

from PIL import Image
from PIL.ExifTags import TAGS

import glob
import operator

class ExifNotFoundError(Exception):
    """Raised when no Exif data has been found

    Attributes:
        filename The filename being analyzed
        message Overridable exception message
    """
    def __init__(self, filename, message='No Exif found for'):
        self.message = '{} {}'.format(message, filename)


def get_exif(fn):
    exif = {}
    i = Image.open(fn)
    info = i._getexif()

    if info is None:
        raise ExifNotFoundError(fn)

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif[decoded] = value

    return exif

def get_focal_length(exif):
    return exif['FocalLength'][0]

if __name__ == '__main__':
    fls = {}
    count = 0
    for fname in glob.iglob('/Users/mattmusc/Desktop/**/*.dng', recursive=True):
        count += 1
        try:
            fl = get_focal_length(get_exif(fname))
            if fl in fls:
                fls[fl] = fls[fl] + 1
            else:
                fls[fl] = 1
        except ExifNotFoundError as err:
            print(err.message)

    print('Total files analyzed: {}'.format(count))
    print('Focal Lengths:')
    print(sorted(fls.items(), key=operator.itemgetter(1), reverse=True))


