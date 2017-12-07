def first_unique(a):
    n = len(a)
    
    list = []
    
    lst_cnt =1 
    
    visited = [-1]*256
    
    visited[ord(a[0])] = 0
    
    for i in range(1, n):
        
        prev_visit = visited[ord(a[i])]
        
        if prev_visit == -1:

            if lst_cnt == 1:
                return a[i-1]
            
            if lst_cnt > 1 and i == n-1:
                return a[i]
            
            lst_cnt = 1
        else:
            lst_cnt += 1
            
        visited[ord(a[i])] = 1
        

print first_unique('aaaaaayyyyykkc')
