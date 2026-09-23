class Solution(object):
    def maximumWealth(self, accounts):
        count=0
        r=[]
        for i in range(len(accounts)):
            for j in accounts[i]:
                count+=j
            r.append(count)
            count=0
        return max(r)
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        