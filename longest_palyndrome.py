def reverse(str):
    list = []

    a = len(str)-1

    for i in range(a,-1,-1):
        list.append(str[i])
    
    str_reverse = ''.join(list) 
    
    return str_reverse

import collections
def longestPalindrome(s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        for k, v in collections.Counter(s).iteritems():
            print k , v
            odds += v & 1
        print odds
        return len(s) - odds + int(odds > 0)

 
a = palyndrome('forgeeksskeegfor')
print a
 
