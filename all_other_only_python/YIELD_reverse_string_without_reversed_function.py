def rev_str(s):

    s_len = len(s)
    s_new = ''

    for i in xrange(s_len-1,-1,-1):
        yield s[i]
      


print rev_str('partha deka')
