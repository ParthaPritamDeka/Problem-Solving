class get_char:
    def __init__(self, number):
        self.number = number
        
    def get_charac(self):
        
        string = []
        
        while self.number > 0:
            rem = self.number%26
            if rem == 0:
                string.append('Z')
                self.number = self.number/26 -1
            else:
                string.append(chr((rem-1) + ord('A')))
                self.number = self.number/26
                
        string = string[::-1]
        return ''.join(string)
                
get_obj = get_char(28)  
print get_obj.get_charac()
