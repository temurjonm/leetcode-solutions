class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(combo, left, right):
            if len(combo) == 2 * n:
                result.append(''.join(combo))
                return

            if left < n:
                combo.append('(')
                backtrack(combo, left+1, right)
                combo.pop()
            if right < left:
                combo.append(')') 
                backtrack(combo, left, right+1)
                combo.pop()

        backtrack([], 0, 0)

        return result