class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        rows, cols = len(image), len(image[0])

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def visit(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original:
                return

            image[r][c] = color

            for dr, dc in directions:
                visit(dr+r, dc+c)

        visit(sr, sc)

        return image