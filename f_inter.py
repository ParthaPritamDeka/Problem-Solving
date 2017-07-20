'''
Python Questions -

1) Print Max element of a given list
2) Print median of a given list
3) Print the first nonrecurring element in a list
4) Print the most recurring element in a list
5) Greatest common Factor  
'''

def max_element(list):
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

#print max_element([1,2,3,4,5,6])

def median(list):
    n = len(list)
    if n % 2 == 1:
        return list[n/2]

    else:
        print n/2+1
        return sum(list[n/2-1:n/2+1])/2
    
def nonrecur(list):
    dict = {}
    for i in range(len(list)):
        if list[i] not in dict:
            dict[list[i]] = 1
        else:
            dict[list[i]] += 1
            
    for i in range(len(list)):
        if dict[list[i]] == 1:
            return list[i]
        
#print nonrecur([1,1,2,2,'a',3,4,4,5,5,6,6,7])
           
def mostrecur(list):
    dict = {}
    for i in range(len(list)):
        if list[i] in dict:
            dict[list[i]] += 1
        else:
            dict[list[i]] = 1
    #print dict  
    
    max_v = 0        
    for k, v in dict.iteritems():
        if v > max_v:
            max_v = v
            max_k = k
    #print max_v
    return max_k
        
print mostrecur([1,1,2,2,'a',3,4,4,5,5,6,6,6,7])       

def GCF(x, y):
    
    if x > y :
        smaller = y
    else:
        smaller = x
        
    for i in range(1, smaller+1):
        if (x%i) == 0 and (y%i) == 0:
            gcf = i
    return gcf
        
