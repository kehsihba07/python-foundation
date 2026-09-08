class Solution(object):
    def countDigits(self, num):
        count=0
        for d in str(num):
            val=int(d)
            if num%val==0:
                count+=1
        return count   