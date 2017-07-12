def max_sum_mul(string1):
    list_num = [int(x) for x in string1]
    max_sum = 0
    max_mul = 1
    max_all = 0
    for i in range(len(list_num)):
        
        '''
        for j in range(len(list_num)):
            if list_num[i] == list_num[j]:
                pass
            else:
                
                sum_now = max_sum + list_num[i] + list_num[j]
                mul_now = max_mul*list_num[i]*list_num[j]
                if sum_now > max_sum:
                    max_sum = sum_now
                if mul_now > max_mul:
                    max_mul = mul_now
                if max_mul > max_sum:
                    max_all = max_mul
                else:
                    max_all = max_sum
        '''
       
        if (list_num[i] + max_sum) > max_sum:
            max_sum = list_num[i] + max_sum
        if (list_num[i]*max_mul) > max_mul:
            max_mul = list_num[i]*max_mul
        if max_mul > max_sum:
            max_all = max_mul
        else:
            max_all = max_sum
        
    return max_all
                    
                
print max_sum_mul('212')
