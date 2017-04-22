
def chck_uniq_char(s):

    # s= 'aabcdee'

    for i in s:
        cnt_char = s.count(i)
        if cnt_char >1:
            return False

    return True

print chck_uniq_char('abcdef')
