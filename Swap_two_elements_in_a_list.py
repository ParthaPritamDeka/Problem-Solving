def swap_two_elements(list, a, b):
    
    x , y = list.index(a), list.index(b)
    
    list[y], list[x] = list[x], list[y]
    
    return list

print swap_two_elemenst(['abcd','dcba','dbac','xyz','zxy','yzx','adbc', 'xyza'] ,'xyz', 'abcd')
