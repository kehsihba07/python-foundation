class Solution(object):
    def isAnagram(self, s, t):
        c=0
        for i in range(len(s)):
            if s.count(s[i])==t.count(s[i]):
                c+=1
        if c==len(t) and c==len(s):
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        