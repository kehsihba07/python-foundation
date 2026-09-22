class Solution(object):
    def addDigits(self, num):
        while num>=10:
            count=0
            for n in str(num):
                y=int(n)
                count+=y
            num=count
        return num
        """
        :type num: int
        :rtype: int
        """
        