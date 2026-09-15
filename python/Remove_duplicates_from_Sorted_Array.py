class Solution:
    def removeDuplicates(self, arr):
        r = []
        seen = set()

        for n in arr:
            if n not in seen:
                r.append(n)
                seen.add(n)

        return r
        