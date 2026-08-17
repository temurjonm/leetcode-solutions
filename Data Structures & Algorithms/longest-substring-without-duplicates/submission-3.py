class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        total = 0
        # base cases
        if not s:
            return 0
        # use ds hash set + sliding window
        seen = set()
        left  = 0

        # iterate over string 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            total = max(total, right - left + 1)

        return total