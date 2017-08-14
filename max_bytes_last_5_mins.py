'''
Timestamp   Src IP Addr:Port  Dst IP Addr:Port  Bytes
1502475666  10.0.0.1:24920    10.0.0.2:443      10
1502475666  10.0.0.3:24921    10.0.0.2:443      20
1502475666  10.0.0.3:24921    10.0.0.2:443      20
1502475666  10.0.0.3:24921    10.0.0.2:443      20
1502475666  10.0.0.3:24921    10.0.0.2:443      20
1502475666  10.0.0.3:24921    10.0.0.2:443      20
'''

import time

def parser(st):
    
    
    
    #f = open(str, 'rU')
    '''
    max_byte = 1
    lst_time =  1
    lst_src_ip = '10.0.0.0.2:443'
    lst_trg_ip = '10.0.0.0.2:443'
    '''
    
    
    dict_max_byte =  {}
    
    now = time.time() 
    
    lst_5 = now - 300
    
    sum_byte = 0
    
    for line in st.split('\n'):
        list1 = st.split('\t')
        byte = list1[3]
        if (list1[1], list1[2]) not in dict_max_byte and list1[0] >= lst_5 and list1[0] <= now::
            dict_max_byte[(list1[1], list1[2])] = byte
        
        if ((list1[1], list1[2]) in dict_max_byte) and list1[0] >= lst_5 and list1[0] <= now:
            #if (list1[1], list1[2]) in dict_max_byte:
               sum_byte += byte
               dict_max_byte[(list1[1], list1[2])] = sum_byte
            
    return dict_max_byte
            
            
                
   print def parser("") 
