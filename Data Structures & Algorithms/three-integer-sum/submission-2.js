class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    /*
        [-1,0,1,2,-1,-4].sort()
        [-4,-1,-1,0,1,2]
          i
             l      
                      r  
         

    */
    threeSum(nums) {
        nums.sort((a,b) => a-b);
        let result = []
        for (let i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] === nums[i-1]) continue

            let left = i+1, right = nums.length - 1

            while (left < right) {
                let total = nums[i] + nums[left] + nums[right]

                if (total === 0) {
                    result.push([nums[i], nums[left], nums[right]])
                    left++
                    while (left < right && nums[left] === nums[left-1]) left++

                } else if ( total < 0) {
                    left++
                } else {
                    right --
                }
            }
        }

        return result
    }
}
