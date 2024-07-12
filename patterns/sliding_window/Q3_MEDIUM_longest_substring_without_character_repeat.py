

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        charset = set()
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            ans = max(ans, right - left + 1)
        return ans