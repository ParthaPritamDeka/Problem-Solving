import random

def generate_random():
    for i in range(6):
        yield random.randint(1, 40)

 

for random_number in generate_random():
    print "And the next number is....%d!" % random_number
