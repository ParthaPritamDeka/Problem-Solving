#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This and the following exercise are using US Patent database.
# The patent.data file is a small excerpt of a much larger datafile
# that is available for download from US Patent website. They are pretty large ( >100 MB each).
# The data itself is in XML, however there is a problem with how it's formatted.
# Please run this script and observe the error. Then find the line that is causing the error.
# You can do that by just looking at the datafile in the web UI, or programmatically.
# For quiz purposes it does not matter, but as an exercise we suggest that you try to do it programmatically.
# The original file is ~600MB large, you might not be able to open it in a text editor.

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

PATENTS = 'patent_xml.xml'

'''
def get_root(fname):

    tree = ET.parse(fname)
    return tree.getroot()
'''

def analyze(xml):
    #it = ET.iterparse(file(xml))
    count = 0
    last = None

    try:        
        for (ev, el) in ET.iterparse(file(xml)):
            
            count += 1
            last = el

    except ParseError:
            print("catastrophic failure")
            print("last successful: {0}".format(last))

    print('count: {0}'.format(count))

def xmlparse(xml):
    tree = parser.parse(testf)
    for node in tree.iter(xml):
        print node.text

def main():
    analyze(PATENTS)
    #xmlparse(PATENTS)

if __name__ == '__main__':
    main()

