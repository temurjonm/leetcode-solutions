class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def helper(start, comboArray, target):
            if target == 0:
                result.append(comboArray[:])
                return

            elif target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comboArray.append(candidates[i])
                helper(i+1, comboArray, target - candidates[i])
                comboArray.pop()

        helper(0, [], target)

        return result