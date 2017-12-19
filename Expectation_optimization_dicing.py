import random
#print ("Here is the output:" , random.randint(1,6))


def max_expectations(n):

    lst_state = 0
    

    for i in range(n):
        print ("I am dicing:")
        output = random.randint(1,6)
        
        if output == 6:
            print ("I am within the main output loop")
            print ("I have reached my expected number:",  output)
            return 
        
        if output < 6 and lst_state < 6:
            print ("I am within the lst_state loop")
            lst_state = lst_state + output
            if lst_state == 6:
                print ("I have reached my expected number:",  lst_state)
                return 
       
    print ("optimization or mazimization failed:") 
    return
             
