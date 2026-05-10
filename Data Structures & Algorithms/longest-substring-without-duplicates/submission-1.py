class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_subs = 0
        longestSet = set()
        left = 0

        for right, char in enumerate(s):
            while char in longestSet:
                longestSet.remove(s[left])
                left += 1

            longestSet.add(char)
            longest_subs = max(longest_subs, right - left + 1)

        return longest_subs
            