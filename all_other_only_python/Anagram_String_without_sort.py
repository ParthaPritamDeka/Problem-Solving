def string_anagram(s1, s2):

    dict_1 = {}
    dict_2 = {}

    for i in range(len(s1)):
        if s1[i] not in dict_1:
            dict_1[s1[i]] = 1

        else:
            dict_1[s1[i]] +=1

    for j in range(len(s2)):
        if s2[j] not in dict_2:
            dict_2[s2[j]] = 1

        else:
            dict_2[s2[j]] +=1

    print dict_1
    print dict_2

    if dict_1 == dict_2:
        return True

    return False


print string_anagram('paaarthhhhhaaaa', 'thhhhhpaaraaaa')
        
