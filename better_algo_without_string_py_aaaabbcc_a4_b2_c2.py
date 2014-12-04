'''' Python Passion_coding ''''

def str_cnt_char(s):

    list = []
    for i in range(len(s)):
        if s[i] not in list:
             list.append(s[i])
             cnt = s.count(s[i])
             list.append(str(cnt))
    print list
    new_string = ''.join(list)
    return new_string

print str_cnt_char('aaaaaabbbbbbbbcccccddddddddd')
