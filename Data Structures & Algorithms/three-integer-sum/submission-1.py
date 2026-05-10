class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        # iterate an array with gap 2
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i+1, len(nums)-1
            while start < end:
                # get total of the 3 sum amd check if is equal to 0
                treeSum = nums[i] + nums[start] + nums[end]

                # check if total == 0 add to the result
                if treeSum == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                elif treeSum < 0:
                    start += 1
                else:
                    end -= 1
        return result  
