def rows(n):
    #for i in range(n):
    i = 0
    dict = {}
    max_value = 0
    while max_value <= n:
        i = i + 1
        dict[i] = i
        max_value = sum(dict.values())
        last_value = len(dict.keys()) - 1
    return last_value
        
print rows(21)   
