def funct(str1, str2):
    dict1 = {}
    dict2 = {}
    for i in str1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
        
    for i in str2:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] += 1
    if len(dict1.keys()) > len(dict2.keys()):
        return set(dict1.keys()) > set(dict2.keys())
    else:
        return set(dict2.keys()) > set(dict1.keys())
    
print funct('abcxy','abcdefgxy')