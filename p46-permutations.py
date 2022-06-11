class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        oldperm = []
        newperm = []
        for i in nums:
            if oldperm == []:
                oldperm.append([i])
                continue
            for j in oldperm:
                newperm.append(j + [i])
                newperm.append([i]+j)
                for k in range(1, len(j)):
                    newperm.append(j[:k]+[i]+j[k:])
            oldperm = newperm
            newperm = []
        return oldperm
