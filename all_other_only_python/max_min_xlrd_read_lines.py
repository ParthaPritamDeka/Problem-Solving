#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
import pprint
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    data = []
    
    list = sheet.col_values(1, start_rowx=1, end_rowx=None)
    
    maxval = max(list)
    minval = min(list)

    maxpos = list.index(maxval) + 1
    minpos = list.index(minval) + 1

    maxtime = sheet.cell_value(maxpos, 0)
    maxrealtime = xlrd.xldate_as_tuple(maxtime, 0)

    mintime = sheet.cell_value(minpos, 0)
    minrealtime = xlrd.xldate_as_tuple(mintime, 0)

    data = {
            'maxtime': maxrealtime,
            'maxvalue': maxval,
            'mintime': minrealtime,
            'minvalue': minval,
            'avgcoast': float(sum(list))/ float(len(list))
    }
    return data

            
def test():
    #open_zip(datafile)
    data = parse_file(datafile)
    pprint.pprint(data)

    #assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    #assert round(data['maxvalue'], 10) == round(18779.02551, 10)


if __name__ =='__main__':
    test()
