class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        colorlist = []
        colorlist = self.floodhelper(image, sr, sc, color, [])
        for i in colorlist:
            image[i[0]][i[1]] = newColor
        return image

    def floodhelper(self, image: List[List[int]], row: int, column: int, color: int, result: List[List[int]]) -> List[List[int]]:
        if [row, column] in result:
            return result
        result.append([row, column])
        if row > 0 and image[row-1][column] == color:
            result = self.floodhelper(image, row-1, column, color, result)
        if row < len(image)-1 and image[row+1][column] == color:
            result = self.floodhelper(image, row+1, column, color, result)
        if column > 0 and image[row][column-1] == color:
            result = self.floodhelper(image, row, column-1, color, result)
        if column < len(image[0])-1 and image[row][column+1] == color:
            result = self.floodhelper(image, row, column+1, color, result)
        return result
