def target_two(num_list, target):
    
    if len(num_list)<= 1:
        return False
    
    buff_dict = {}
    return_list = []
    
    for i in range(len(num_list)):
        if num_list[i] in buff_dict:
            return_list.append((buff_dict[num_list[i]], num_list[i]))
        else:
            buff_dict[target-num_list[i]] = num_list[i]
                               
    return return_list
buff_dict = {-4 : 0, -3 : 1, 3 : 2}
