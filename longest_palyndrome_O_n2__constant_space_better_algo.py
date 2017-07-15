def logestpalyndrome(str):
    maxlength = 1
    
    start = 0
    length = len(str)
    
    low = 0
    high = 0
    
    for i in range(1, length):
        
        #find longest even length palyndrome
        low = i - 1
        high = i
        while low >=0 and high < length and str[low] == str[high]:
            if high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
                
            low = low -1
            high = high + 1
            
        #find longest odd palyndrome
        
        low = i -1
        high = i + 1
        
        while low >= 0 and high < length and str[low] == str[high]:
            if high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
            low = low -1
            high = high + 1
            
            
    return str[start: start + maxlength]      
