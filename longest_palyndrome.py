def reverse(str):
    list = []

    a = len(str)-1

    for i in range(a,-1,-1):
        list.append(str[i])
    
    str_reverse = ''.join(list) 
    
    return str_reverse

def palyndrome(s):
    list = []
    for i in range(len(s)):
        for j in range(i+1,len(s),1):
            str_1 = s[i:j+1]
            if len(str_1) > 1:
                #print str_1
                str_rev = reverse(str_1)
                #print str_rev
                if str_rev == str_1:
                    num = int(len(str_1))
                    tup = (str_1,num)
                    list.append(tup)
    #print list
    max_cnt = 0
    for (m, n) in list:
        if n > max_cnt:
            max_cnt = n
            max_str = m
    
    return max_str

 
a = palyndrome('forgeeksskeegfor')
print a
 
