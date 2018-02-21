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
