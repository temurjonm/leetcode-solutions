class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hasDuplicate = new Set();
        
        for (const num of nums) {
            if (hasDuplicate.has(num)) return true
            hasDuplicate.add(num)
        }
        return false
        
    }
}
