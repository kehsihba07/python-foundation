class Solution(object):
    def runningSum(self, nums):
        a=[]
        y=0
        for n in nums:
            y=y+n
            a.append(y)
        return a