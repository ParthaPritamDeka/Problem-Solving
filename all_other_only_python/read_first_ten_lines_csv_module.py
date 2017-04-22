import re
import csv
import pprint
def parse_file(datafile):
    
    data = []
    f = open(datafile) 
    counter = 0
    r = csv.DictReader(f)
    for line in r:
        if counter == 10:
           break
        data.append(line)
        counter += 1
        #if counter == 1:
          # break
    return data
        
    
def main():
    d = parse_file('C:\\Python27\\beatles-diskography.csv')
    pprint.pprint(d)
    #print parse_file('C:\\Python27\\beatles-diskography.csv')




if __name__ =='__main__':
    main()
