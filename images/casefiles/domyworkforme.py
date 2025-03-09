#!/usr/bin/env python3

import urllib.parse
import glob

filenames = glob.glob('*')

for filename in filenames:
    text = urllib.parse.quote(filename)
    print( '<img src="%s" loading="lazy">' % text)
