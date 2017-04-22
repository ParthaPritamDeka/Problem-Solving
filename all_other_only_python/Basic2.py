# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.



def single_element(list):
    
    list_new = []

    for i in list:
        if len(list_new) == 0 or i != list_new[-1]:
            list_new.append(i)

    return list_new         
           


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

def linear_merge(list1, list2):

    merge_list = []

    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            merge_list.append(list1.pop(0))
        else:
            merge_list.append(list2.pop(0))

    merge_list.extend(list1)
    merge_list.extend(list2)
    return merge_list
        
    



    
 

def main():

    #print single_element([1,2,2,3,3,4])

    print linear_merge([2,3,4,5,6,7,8,9],[6,7,8,9,10])

if __name__ == '__main__':

    main()
