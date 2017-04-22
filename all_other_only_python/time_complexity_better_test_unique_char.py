def chck_uniq_char(s):

    # s= 'aabcdee'
    u_chars = set()

    for i in s:
        if i in u_chars:
            #print u_chars
            return False
        
        u_chars.add(i)
    #print u_chars
    return True

#print chck_uniq_char('adbcefghauigqeuifufduihjjkduvhfvyugeygggefigeighghgvvhvjhvejhfvhegvhhdfvhvhvfbbbhjdcbhbhvdbhvhfhgyuhduigfdhhgbvhfhvbhbfvhhfbhgvhkjbhvb')

print chck_uniq_char('abcdefghijkl')
