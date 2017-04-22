def largest_continous_sum(list):

    if len(list) == 0:
        return

    maxnum = list[0]
    currentsum = list[0]

    if len(list) == 1:
        maxnum = list[0]
        return maxnum

   

    for num in list[1:]:
        currentsum = max(currentsum+num, num)
        maxnum = max(maxnum, currentsum)

    return maxnum

print largest_continous_sum([-2, 6, 3, 4, 5])


























        
