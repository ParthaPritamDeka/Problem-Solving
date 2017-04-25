"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(array, value):
    """Your code goes here."""
    lower = 0
    upper = len(array)
    
    while lower < upper:
        
        x = lower + (upper - lower) /2
        print "this teration"
        print x
        
        val = array[x]
        
        if target == val:
            return x
        
        elif target > val:
            if lower == x:
                return -1
            
            lower = x
            
        else:
            upper = x
    return -1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
