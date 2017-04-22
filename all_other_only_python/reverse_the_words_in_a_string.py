def rev_words(s):

    #s ='partha.deka'
    list = s.strip().split('\\')
    list.reverse()
    
    new_string = '\\'.join(list)

    return new_string

print rev_words('partha\deka')
