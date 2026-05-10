class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let myMap = new Map()

        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i]

            if (myMap.has(diff)) {
                return [myMap.get(diff), i]
            }

            myMap.set(nums[i], i) 
        }
    }
}
