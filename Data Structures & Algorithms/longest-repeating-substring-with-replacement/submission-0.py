class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqCount = {}
        longest_subs = 0
        left = 0

        for right, char in enumerate(s):
            freqCount[char] = freqCount.get(char, 0) + 1

            if (right - left + 1) - max(freqCount.values()) > k:
                freqCount[s[left]] -= 1
                left += 1

            longest_subs = max(longest_subs, right - left + 1)

        return longest_subs
