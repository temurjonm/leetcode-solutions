'''
"pwwkew"
 l
   r
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = longestSub = 0

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)   
            longestSub = max(longestSub, right - left + 1)
        
        return longestSub