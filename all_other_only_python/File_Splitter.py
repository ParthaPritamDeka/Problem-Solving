
import os
import pymadlib

actual_file = 'patent_xml_to_split.xml'

def find_boundaries(doc):
    idx = 0
    for line in doc:
        if line.startswith("<?xml"):
            yield idx
        idx += 1
    yield idx

def split_file(filename):

    f = open(filename, "r")
    doc = f.readlines()
    print len(doc)
    for m in range(len(doc)):
        print m

    boundaries = list(find_boundaries(doc))
    # boundaries = [0, 10, 20, 30, 40]
    print boundaries

    i, j = 0, 1
    for n in range(len(boundaries) - 1):
        with open('{}-{}'.format(filename, n), 'w') as f:
            f.writelines(doc[boundaries[i]:boundaries[j]])
            print boundaries[i], boundaries[j]
        i += 1
        j += 1


def main():

    split_file(actual_file)




if __name__ =='__main__':
    main()
        
