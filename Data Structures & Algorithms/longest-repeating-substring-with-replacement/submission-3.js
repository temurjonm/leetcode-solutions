class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     * 
     * "XYYX"
     *  L
     *  R
     */
    characterReplacement(s, k) {
        let longest = 0, left = 0
        let hashMap = new Map()
        let maxCount = 0

        for (let right = 0; right < s.length; right++) {
            let charRight = s[right]
            hashMap.set(charRight, (hashMap.get(charRight) || 0) + 1);
            maxCount = Math.max(maxCount, hashMap.get(charRight));

            if ((right - left + 1) - maxCount > k) {
                let charLeft = s[left]
                hashMap.set(charLeft, hashMap.get(charLeft) - 1);
                left++
            }
            longest = Math.max(longest, right - left + 1)
        }

        return longest
    }
}
