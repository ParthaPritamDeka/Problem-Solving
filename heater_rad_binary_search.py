'''
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
'''
'''
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
'''

def binary_search(array, target):
    """Your code goes here."""
    lower = 0
    upper = len(array)
    
    while lower < upper:
        
        x = lower + (upper - lower) /2
        #print "this teration"
        #print x
        
        val = array[x]
        
        if target == val:
            return x
        
        elif target > val:
            if lower == x:
                return -1
            
            lower = x
            
        else:
            upper = x
    return -1

def heater_rad(ho,hea):
    
    ho = sorted(ho)
    n_ho = len(ho)
    hea = sorted(hea)
    n_hea = len(hea)
    
    prev_dis = 0
    
    if n_hea == 0:
        return 0
    
    elif n_hea == 1:
        pos = binary_search(ho, hea[0])
        if (n_ho - pos -1) > pos:
            max_dis = n_ho - 1 - pos
        else:
            max_dis = pos
        return max_dis
    else:   
        for j in range(len(hea)):
            new_dis = binary_search(ho, hea[j])
            if new_dis - prev_dis > prev_dis:
                prev_dis = new_dis - prev_dis
        max_dis = prev_dis
        
        if max_dis%2 == 0:
            rad = max_dis / 2
            return rad
        else:
            rad = max_dis / 2 + 1
            return rad
        
    #print max_dis
    
    
            
    
    #print dict
    #for i in range(n_ho):
        
print heater_rad([1,2,3,4,5,6,7],[2, 5]) 
