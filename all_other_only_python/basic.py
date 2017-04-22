
#A

def match_end(strings):

    count = 0

    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1

    return count


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.


def front_x(strings):

    #list_x = []
    #list_abc = []
    

    #for string in strings:
        #if string[0].lower() == 'x':
           # list_x.append(string)

        #else:
            #list_abc.append(string)

    #return sorted(list_x) + sorted(list_abc)
         
     list_x = [s for s in strings if s.startswith('x')]
     list_nonx = [s for s in strings if not s.startswith('x')]

     return sorted(list_x) + sorted(list_nonx)


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

def get_key(tuple):

    tup_len = len(tuple)

    return tuple[tup_len-1]

def sort_last(tuples):

    return sorted(tuples, key=get_key)


    



def main():
    #print match_end(['aba', 'cdc', 'abc'])

    #print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])

    print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])




if __name__ == '__main__':

    main()
