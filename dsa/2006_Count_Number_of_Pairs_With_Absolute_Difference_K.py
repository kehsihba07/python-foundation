class Solution(object):
    def countKDifference(self, nums, k):
        c = 0
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    c += 1
        return c