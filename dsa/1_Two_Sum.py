class Solution(object):
    def twoSum(self, arr, target):
        r = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    r.append(i)
                    r.append(j)
                    return r