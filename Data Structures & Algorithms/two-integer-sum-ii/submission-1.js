class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    /*
        [1,2,3,4], target = 3
         i
           j
        5 > 3 right--
        4 > 3 right--
        3 == 3 return [i+1, j+1]

     */
    twoSum(numbers, target) {
        let left = 0, right = numbers.length - 1

        while (left < right) {
            let total = numbers[left] + numbers[right]

            if (total == target) {
                return [left+1, right+1]
            } else if (total < target) {
                left++
            } else {
                right--
            }
        }
    }
}
