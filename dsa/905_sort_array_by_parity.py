class Solution(object):
    def sortArrayByParity(self, nums):
        r=[]
        y=[]
        for n in nums:
            if n%2==0:
                r.append(n)
            else:
                y.append(n)
        return r+y
        