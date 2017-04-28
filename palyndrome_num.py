def palyndrom_num(num):
    
    reverse = 0
    
    while (num>0):
        reminder = num % 10
        reverse = reverse*10 + reminder
        num = num // 10
        
    print reverse  
    
    if int(reverse) == int(num):
        return True
    else:
        return False

print palyndrom_num(5445)