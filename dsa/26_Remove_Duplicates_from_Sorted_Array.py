class Solution(object):
    def removeDuplicates(self, nums):
        r=[]
        for n in nums:
            if n not in r:
                r.append(n)
        for i in range(len(r)):
            nums[i]=r[i]
        return len(r)
        """
        :type nums: List[int]
        :rtype: int
        """
        