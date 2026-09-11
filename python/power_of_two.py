class Solution:
    def isPowerofTwo(self, n):
        for i in range(0,n):
            if 2**i==n:
                return True
        return False    