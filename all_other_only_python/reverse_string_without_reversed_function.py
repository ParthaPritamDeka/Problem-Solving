def rev_str(s):

    s_len = len(s)
    s_new = []

    for i in xrange(s_len-1,-1,-1):
        s_new.append(s[i])

    return ''.join(s_new)

print rev_str('partha deka')
