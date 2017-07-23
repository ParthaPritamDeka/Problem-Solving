def longest(a):
    
    n = len(a)
    
    list = []
    
    last_cnt = 1
    
    visited = [-1]*256
    
    #lets keep the first element as visited
    
    visited[ord(a[0])] = 0
    
    for i in range(1, n):
        
        prev_visit = visited[ord(a[i])]
        
        if prev_visit == -1:
            if last_cnt == 1:
                return a[i-1]
            last_cnt = 1
            
        else:
            last_cnt +=1
            
        visited[ord(a[i])] = i
        

print longest('aaaaaayyyyykcbbffffxxxxxx')
