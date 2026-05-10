class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(start, subset):
            sortedSubset = sorted(subset[:])
            if sortedSubset not in result:
                result.append(sortedSubset)

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtracking(i+1, subset)
                subset.pop()

        backtracking(0, [])

        return list(result)