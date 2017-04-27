def func(X):
    list = []
    dict = {}
    
    for i in range(len(X)):
        if X[i] not in dict:
            dict[X[i]] = str(X.count(X[i]))
            kv = str(X[i]) + str(dict[X[i]])
            list.append(kv)
    str_num = ''.join(list)
    print str_num
    
    dict_1 = {}
    
    lst_num_cnt = 0
    
    lst_str = ''
    str_add = ''
    cnt = 0
    prev_num = 0
    
    for i in range(1, len(str_num), 2):
        
        print str_num[i]
        if int(str_num[i]) > 1:
            
            if lst_num_cnt == 0:
                lst_num_cnt =+ 1
                print "10 "
                print lst_num_cnt
                str_add = str_add + str_num[i-1]
                print str_add
                dict_1[str_add] = 1
                prev_num = int(str_num[i])
                
            elif lst_num_cnt == 1:
                lst_num_cnt = lst_num_cnt + 1
                print "11 "
                print lst_num_cnt
                str_add = str_add + str_num[i-1]
                print str_add
                dict_1[str_add] = 1
                str_add = str_num[i-1]
                prev_num = int(str_num[i])
            
            elif lst_num_cnt > 1:
                lst_num_cnt = lst_num_cnt + 1
                str_add = str_add + str_num[i-1]
                print "12"
                print str_add
                dict_1[str_add] = 1
                str_add = str_num[i-1]
                print str_add
                prev_num = int(str_num[i])
            else:
                pass
                
        elif int(str_num[i]) == 1:
            print "prev_num"
            print prev_num
            print lst_num_cnt
            if lst_num_cnt == 0 and prev_num > 1:
                str_add = str_num[i-3]
                print str_add
                
            print "in this loop main"
            if lst_num_cnt >= 1:
                print "20"
                str_add = str_add + str_num[i-1]
                print str_add
                dict_1[str_add] = 1
                #str_add = X[i-1]
                lst_num_cnt = 0
                prev_num = int(str_num[i])
                
            else:
                print "21"
                str_add = str_add + str_num[i-1]
                print str_add
                dict_1[str_add] = 1
                prev_num = int(str_num[i])
            
        else:
            pass
            
    return dict_1 

print func('aaabbcccdddfghijjjjk')