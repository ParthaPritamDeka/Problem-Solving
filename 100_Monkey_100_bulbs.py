# 100 monkeys turning off/ on 100 bulbs skipping one one at a time 

num_monkeys =100

n = num_monkeys + 1

switch_state = n*[0]

Monkey_list = n*[1]

for i in range(len(Monkey_list)):
    i = i + 1
    if i == 1:
        for j in range(len(switch_state)):
            j = j + 1
            if j > n-1:
                break
            switch_state[j] = 1
        #print switch_state[1:n]
    
    else:
        for j in range(i,len(switch_state),2):
            #print j
            if j > n-1:
                break
            if switch_state[j] == 0:
                switch_state[j] = 1
            else:
                switch_state[j] = 0
        #print ' '
        #print switch_state[1:n]
                
#print switch_state
        
print len([x for x in switch_state[1:n] if x == 1])


#### Simple solution:

monkey = 100*[1]

switch_state = 100*[0]

for m in range(0,100,1):
    for s in range(m,100,2):
        if switch_state[s] == 0:
            switch_state[s] = 1
        else:
            switch_state[s] = 0
            
print len([x for x in switch_state[0:100] if x == 1])

print switch_state
    

    
