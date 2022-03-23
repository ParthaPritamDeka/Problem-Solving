def ispalyndrome(s):
    
#     for i in range(0, len(s)//2):
#         if str[i] != str[len(s)-1-i]:
#             return False
#     return True

    i = 0
    j = len(s)-1
    
    while i < j:
        print ('s[i] ',s[i])
        print ('s[j] ',s[j])
        print ('=======')
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
   
    return True
