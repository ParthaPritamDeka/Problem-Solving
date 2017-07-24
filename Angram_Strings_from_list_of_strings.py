def anagram(list):
    dict = {}
    list_new = []
    for i in range(len(list)):
        sort_element = ''.join(sorted(list[i]))
        if sort_element in dict:
            if prev_element == sort_element:
                list_new.append(list[prev_index])
                prev_element = None
            dict[sort_element] += 1
            list_new.append(list[i])
            
        else:
            dict[sort_element] = 1
            prev_element = sort_element
            prev_index = i
    
    
    return list_new  
                
print anagram(['abcd','dcba','dbac','xyz','zxy','yzx','adbc', 'xyza'])  
