class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, comboArray, target):
            if target == 0:
                result.append(comboArray[:])
                return
            elif target < 0:
                return

            for i in range(i, len(nums)):
                comboArray.append(nums[i])
                dfs(i, comboArray, target - nums[i])
                comboArray.pop()

        dfs(0, [], target)

        return result
