def longest(a):
    n = len(a)
    list = []
    
    last_cnt = 1
    
    visited = [-1]*256
    
    ##I will make the first character as visited
    
    visited[ord(a[0])] = 0
    
    for i in range(1,n):
        
        prev_visit = visited[ord(a[i])]
        
        if prev_visit == -1:
            visited[ord(a[i-1])] = -1
            list.append(a[i-1]+ str(last_cnt))
            last_cnt = 1
            
        else:
            last_cnt += 1
            

        visited[ord(a[i])] = i
        
    list.append(a[i]+ str(last_cnt))   
    
        
    return ''.join(list)

print longest('abbcbbffffxxxxxx')
