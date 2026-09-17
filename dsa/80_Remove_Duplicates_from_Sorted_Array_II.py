class Solution(object):
    def removeDuplicates(self, nums):
        r = []

        for n in nums:
            if len(r) < 2 or n != r[-2]:
                r.append(n)

        for i in range(len(r)):
            nums[i] = r[i]

        return len(r)