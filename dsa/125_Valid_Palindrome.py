class Solution(object):
    def isPalindrome(self, s):
        a="abcdefghijklmnoupqrstuvwxyz0123456789"
        b=""
        for n in s.lower():
            if n in a:
                b+=n
        if b[::-1]==b: 
            return True
        else:
            return False

        """
        :type s: str
        :rtype: bool
        """
        