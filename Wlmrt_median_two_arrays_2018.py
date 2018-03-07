def median_two_sorted(list1, list2):
    list_two = list1 + list2
    
    
    list_two = sorted(list_two)
    
    
    n = len(list_two)
    
    while n%2 == 1:
        return list_two[n//2]
        
    else:
        return float(float(list_two[n//2-1] + float(list_two[n//2]))//2
        
 # [1,2,3,4,5,] [3,4,5]
       3
 #[3,4,5,6,7] . [3,4,5]
 

       5
n -> n/2 -> n/4
log(n)
        
   1 2 3 3 4 4 5 5 6 7  
   
       3 3 4 4 5 5
 def median(ar1, ar2, n):
     i = 0
     j = 0
     
     m1 = -1
     m2 = -1
     
     count = 0
     while count < n + 1:
         count += 1
         
         
         if i == n:
             m1 = m2
             m2 = ar2[0]
             break
         
         elif j == n:
             m1 = m2
             m2 = ar1[0]
             break
             
         if ar1[i] < ar2[j]:
             m1 = m2
             m2 = ar1[i]
             i += 1
             
         else:
             m1 = m2
             m2 = ar2[j]
             j =+ 1
             
       return (m1+m2)/2
         
         
         
         
         
         
         
         
         
           
     
