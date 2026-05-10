class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(permuteArray = []):
            if len(permuteArray) == len(nums):
                result.append(permuteArray[:])


            for num in nums:
                if num not in permuteArray:
                    permuteArray.append(num)
                    dfs(permuteArray)
                    permuteArray.pop()


        dfs([])

        return result