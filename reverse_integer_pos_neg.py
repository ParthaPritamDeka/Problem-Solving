def reverse_int(num):
    reverse = 0
    if int(num) > 0:
        while (num>0):
            reminder = num % 10
            reverse = reverse*10 + reminder
            num = num // 10
        return reverse
    
    else:
        num = int(str(num).split('-')[1])
        while (num>0):
            reminder = num % 10
            reverse = reverse*10 + reminder
            num = num // 10
        reverse = int(str('-'+str(reverse)))
        return reverse


print reverse_int(-1234)