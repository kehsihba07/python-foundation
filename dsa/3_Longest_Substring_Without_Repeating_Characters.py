class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left += 1

            st.add(s[right])
            ans = max(ans, right - left + 1)

        return ans