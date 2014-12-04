def char_maxcnt(s):

    max_cnt = 0
    for i in s.lower():
        j = s.lower().count(i)
        if j > max_cnt:
           max_cnt = j
    return max_cnt

print char_maxcnt('paaaaaaaaaaaaaaaaaaaarthhhhhhhhhhhhhhha')
