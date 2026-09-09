class Solution(object):
    def subtractProductAndSum(self, n):
        p=1
        s=0
        for num in str(n):
            y=int(num)
            p=p*y
            s=s+y
        return p-s
        
        