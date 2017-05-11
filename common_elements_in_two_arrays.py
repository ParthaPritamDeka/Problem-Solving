def common_elemnts(list1, list2):
    dict = {}
    list = []
    for i in range(len(list1)):
        if list1[i] in dict:
            dict[list1[i]] =+ 1
        else:
            dict[list1[i]] = 1
            
    for j in range(len(list2)):
        if list2[j] in dict:
            dict[list2[j]] = 0
        else:
            pass
        
    for k, v in dict.items():
        if v == 0:
            list.append(k)
    return ''.join(list)

print common_elemnts(['a','b','b','c','d'], ['c','d','e','f','g','h','i'])