class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        r=[]
        maximum=max(candies)
        for n in candies:
            if n+extraCandies>=maximum:
                r.append(True)
            else:
                r.append(False)