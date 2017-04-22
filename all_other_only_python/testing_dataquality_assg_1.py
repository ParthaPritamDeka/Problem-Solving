

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some 
particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)

def is_int(v):
    try:
        int(v)
        return true
    except ValueError:
        return False
    
def is_float(v):
    try:
        float(v)
        return true
    except ValueError:
        return False

def audit_field(v, fieldtypes):

    v = v.strip()
    print v

    if v == "NULL" or v == "":
        fieldtypes.setdefault(FIELDS[fn], []).append('NoneType')
    elif v.startswith("{"):
        fieldtypes.setdefault(FIELDS[fn], []).append('list')
    elif is_int(v):
        fieldtypes.setdefault(FIELDS[fn], []).append('list')
    elif is_float(v):
        fieldtypes.setdefault(FIELDS[fn], []).append('float')
    else:
        fieldtypes.setdefault(FIELDS[fn], []).append('str')
      

def audit_file(filename, fields):
    fieldtypes = {}

    

    # YOUR CODE HERE
    input_file = csv.DictReader(open(filename))
    skip_lines(input_file,3)
    for row in input_file:
        for fn in range(len(FIELDS)):
            print row[FIELDS[fn]]
            audit_field(row[FIELDS[fn]], fieldtypes)
            
        
        
    
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    #assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    #assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
