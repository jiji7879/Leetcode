class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [[inf for i in mat[0]] for j in mat]
        i=0
        while i < len(mat):
            j=0
            while j < len(mat[0]):
                if mat[i][j] == 0:
                    result[i][j] = 0
                j+=1
            i+=1
        #checking neighbors from left and up
        i=0
        while i < len(mat):
            j=0
            while j < len(mat[0]):
                top = result[i-1][j] if i-1 >= 0 else inf
                left = result[i][j-1] if j-1 >= 0 else inf
                result[i][j] = min(top+1, left+1, result[i][j])
                j+=1
            i+=1
        #checking neighbors from down and right
        i=0
        while i < len(mat):
            j=0
            while j < len(mat[0]):
                bottom = result[-i][-j-1] if -i < 0 else inf
                right = result[-i-1][-j] if -j < 0 else inf
                result[-i-1][-j-1] = min(bottom+1, right+1, result[-i-1][-j-1])
                j+=1
            i+=1
        return result

        
