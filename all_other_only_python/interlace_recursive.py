def str_cat(str1, str2):
    i = 0
    j = 0

    if str1 == '' and str2 == '':
        return

    elif str1 == '':
       return str2

    elif str2 == '':
       return str1

    #x_len = len(str1)
    #y_len = len(str2)
    
    x = str1[0]
    y = str2[0]

    x_rest = str1[1:]
    y_rest = str2[1:]


    return str(x) + str(y) + str(str_cat(x_rest, y_rest))

print str_cat('abc','xyz')


    
        
