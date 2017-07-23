def subset_sum(numbers, target, plist, partial=[]):
    
    s = sum(partial)
    
    if s == target:
        plist.append(partial)
        
    for i in range(len(numbers)):
        n = numbers[i]
        
        remaining = numbers[i+1:]
        subset_sum(remaining, target, plist, partial + [n])
    return plist

if __name__ == '__main__':
    prev_list = []
    print subset_sum([3, 3, 9, 8, 4, 5, 7, 10], 15, prev_list)
