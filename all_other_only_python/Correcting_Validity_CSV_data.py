import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'


def addline(filealt,linetoadd, header):
           with open(filealt, "w") as g:
               writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
               writer.writeheader()
               for i in linetoadd:
                   writer.writerow(i)


def process_file(input_file, output_good, output_bad):
    

    with open(input_file, "r") as f:
         reader = csv.DictReader(f)
         header = reader.fieldnames
         good_list = []
         bad_list  = []
         for line in reader:
             if "dbpedia.org" in line["URI"]:
                elem=line['productionStartYear'][:4]
            
                if elem != 'NULL':
                   print elem
                   yearposs= int(elem)
                   line['productionStartYear']=yearposs 
                   if 1885<yearposs<2015:
                       good_list.append(line)
                      #addline(output_good, line, header)
                   else:
                       bad_list.append(line)
                      #addline(output_bad, line, header)
             print line
             print '\n'
             #except:
                #addline(output_bad, line)
         addline(output_good, good_list, header)
          
         addline(output_bad, bad_list, header)
        

def main():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)

if __name__ =='__main__':
    main()
