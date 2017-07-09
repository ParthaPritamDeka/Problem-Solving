import random
def get_random_item(choices):
    
    #random_index = randrange(0, len(pr))
    #if pr[random_index] <= 0.1:
    
    #choices ={ 0:0.1, 1:0.1, 2:0.8}
    
    space = {}
    current = 0
    
    for choice , wt in choices.iteritems():
        if wt > 0:
            space[current] = choice
            current  += wt
    
    #print space
    rand = random.uniform(0, current)
    #print rand
    #print space.keys(), current
    for key in sorted(space.keys() + [current]):
        if rand < key:
            return choice
        choice = space[key]
 #get_random_item({ 0:0.1, 1:0.1, 2:0.8})       
    
      #return int

sample_dict = {0:0, 1:0, 2:0}
for i in range(0, 100):
    a = get_random_item({0:0.1, 1:0.1, 2:0.8})
    if a in sample_dict:
        sample_dict[a] += 1
print sample_dict
