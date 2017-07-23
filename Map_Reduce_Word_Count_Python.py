##### mapper.py
import sys

for line sys.stdin():
    line = line.strip()
    words = line.split(" ")
    
    for word in word:
        print '%s\t%s' %(word,1)
        
        
###### reducer.py
import sys
current_word = None
current_count = 0
word = None


for line in sys.stdin():
    line = line.strip()
    
    word, count = line.split(" ",1)
    
    try:
        count = int(count)
        
    except ValueError:
        continue
        
    if current_word == word:
        current_count += 1
    
    else:
        if current_word:
            print '%s\t%s' %(current_word, current_count)
            
        current_word = word
        current_count = count
        
if current_word == word:
    print '%s\t%s' %(current_word, current_count)
        
