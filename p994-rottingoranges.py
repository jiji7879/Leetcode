class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == None:
            return 0
        count = -1
        rottenco = []
        rottenconext = []
        onecount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rottenco.append([i,j])
                elif grid[i][j]==1:
                    onecount = 1
        if onecount == 0:
            return 0
        while(rottenco!=[]):
            print(rottenco)
            count += 1
            for item in rottenco:
                if item[0]-1 >=0 and grid[item[0]-1][item[1]]==1:
                    grid[item[0]-1][item[1]]=2
                    rottenconext.append([item[0]-1, item[1]])
                if item[0]+1 < len(grid) and grid[item[0]+1][item[1]]==1:
                    grid[item[0]+1][item[1]]=2
                    rottenconext.append([item[0]+1, item[1]])
                if item[1]-1 >=0 and grid[item[0]][item[1]-1]==1:
                    grid[item[0]][item[1]-1]=2
                    rottenconext.append([item[0], item[1]-1])
                if item[1]+1 < len(grid[0]) and grid[item[0]][item[1]+1]==1:
                    grid[item[0]][item[1]+1]=2
                    rottenconext.append([item[0], item[1]+1])
            rottenco = rottenconext
            rottenconext = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return count
