class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        for i in range(len(nums)):
            for y in range(1,len(nums)):
                if nums[i]==nums[y] and i<y:
                    count+=1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        