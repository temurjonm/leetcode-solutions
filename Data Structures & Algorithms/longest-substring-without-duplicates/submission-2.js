class Solution {
    /**
     * @param {string} s
     * @return {number}
     * 
     * "zxyzxyz"
     *  L
     *    R
     */
    lengthOfLongestSubstring(s) {
        let hashSet = new Set()
        let longest = 0

        let left = 0

        for (let right = 0; right < s.length; right++) {
            while (hashSet.has(s[right])) {
                hashSet.delete(s[left])
                left++
            }
            hashSet.add(s[right])

            longest = Math.max(longest, right - left + 1)
        }

        return longest
    }


}
