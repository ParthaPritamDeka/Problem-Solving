
import re
def word_count(filename, character):

    dict_new = {}

    f = open(filename)
    text = f.read()
    match_text_list = re.findall(r'(\w+)',text)
    #print match_text
    #list = match_text.group().split()
    #print list
    for word in match_text_list:
        if not word in dict_new:
            dict_new[word] = 1
        else:
            dict_new[word] +=1
            
    f.close
    #print match_text_list
    return dict_new[character]
   
    
def main():

    print word_count('C:\\Python27\\basic\\alice.txt' ,'children')




if __name__ =='__main__':
    main()
        
        
