import re
def parse_file(datafile):
    output = {}
    data = []
    f = open(datafile) 
    header = f.readline().split(",")
    counter = 0
    for line in f:
        if counter == 1:
           break
        
        fields = line.strip().split(',')
        
        for i, value in enumerate(fields):
            output[header[i].strip()] = value.strip()
            data.append(output)
        counter +=1
             
    return output
	
    
def main():

    print parse_file('C:\\Python27\\beatles-diskography.csv')




if __name__ =='__main__':
    main()
        
        
