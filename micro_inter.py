
1. how do you iterate one 


2. Write a class, which contains two functions, 1. take query as input, 2. return top 5 queries in the past 1 hour.


### get the top five queries

### 

import operator
from collections import OrderedDict
import itertools
def top_5(query):
       
        i = 0
        new_dict = {}
               
        sorted_list = sorted(query.items(), key=operator.itemgetter(1), reverse = True)
        #print sorted_list
        
        #sorted_dict = OrderedDict(sorted(query.items(), key=operator.itemgetter(1), reverse = True))
        
        #print sorted_dict
        
        top5 = sorted_list[:5]
        
        '''
        for a, b in sorted_dict:
            print a, b
            if i == 5:
                break
            else:
                new_dict[a] = b
                i = i + 1
                
        '''
                    
        return top5 
    
print top_5({'cat' : 4, 'hello': 8, 'weather' : 10, 'partha': 6, 'deka': 7, 'yahoo' : 9, 'indigo': 4})



# Class implementation

import operator
class Top5:
    def __init__(self, query):
        self.query = query
        
    def topFive(self):
        i = 0
        dict1 = {}
        
        sorted_list = sorted(self.query.items(), key=operator.itemgetter(1), reverse = True)
        
        return sorted_list[:5]
        
myobjectx = Top5({'cat' : 4, 'hello': 8, 'weather' : 10, 'partha': 6, 'deka': 7, 'yahoo' : 9, 'indigo': 4})

print myobjectx.topFive()
    
