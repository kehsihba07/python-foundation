class Solution(object):
    def findDifference(self, nums1, nums2):
        r=[]
        s1=list(set(nums1).difference(set(nums2)))
        s2=list(set(nums2).difference(set(nums1)))
        r.append(s1)
        r.append(s2)
        return r
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        