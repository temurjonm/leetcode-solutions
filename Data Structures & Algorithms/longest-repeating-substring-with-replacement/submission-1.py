'''
 "XYYX"
  L
   R

   map = {
        X:1
        Y:1
   }
    getMax= max(getMax, count(curr))

    if (R-L+1) -  getMax > k:
        count(s[l]) -= 1
        L += 1
    return (R - L + 1)

getMax(map) - curr >= k
    res = max(res, right - left + 1)
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqCount = {}
        left = 0
        maxChar = 0

        for right in range(len(s)):
            freqCount[s[right]] = freqCount.get(s[right], 0) + 1
            maxChar = max(maxChar, freqCount[s[right]])

            if (right - left + 1) - maxChar > k:
                freqCount[s[left]] -= 1
                left += 1

        return (right - left + 1)


        