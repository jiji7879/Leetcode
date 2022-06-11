#needed help. Lots of it.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        poslist = []
        neglist = []
        zerocount = 0
        for num in nums:
            if num > 0:
                poslist.append(num)
            elif num < 0:
                neglist.append(num)
            else:
                zerocount += 1
        posset = set(poslist)
        negset = set(neglist)
        solution = set()
        if zerocount >= 3:
            solution.add((0,0,0))
        if zerocount >= 1:
            for i in posset:
                if -i in negset:
                    solution.add((-i,0,i))
        for i, j in combinations(poslist, 2):
            if -(i+j) in negset:
                solution.add(tuple(sorted([-(i+j), i, j])))
        for i, j in combinations(neglist, 2):
            if -(i+j) in posset:
                solution.add(tuple(sorted([-(i+j), i, j])))
        return [list(x) for x in solution]
