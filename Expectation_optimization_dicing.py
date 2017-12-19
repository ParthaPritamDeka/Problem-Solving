import random
#print ("Here is the output:" , random.randint(1,6))


def max_expectations(n):

    #expected = 100
    

    for i in range(n):
        print ("I am dicing:")
        output = random.randint(1,6)
        
        if output == 6:
            print ("I have reached my expected number:",  output)
            return  
       
    print ("I have failed to optimize or mazimize:") 
    return
             
      
            
    #if start == expected:
        #print ("I have reached my expected number:",  start)     
