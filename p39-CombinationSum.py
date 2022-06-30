#check for space later
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        partialcombo = [[] for i in range(target+1)]
        for i in candidates:
            if i <= target:
                partialcombo[i].append([i])
        for i in range(1, target+1):
            for j in candidates:
                if j < i:
                    for k in partialcombo[i-j]:
                        partialcombo[i].append(sorted(k+[j]))
            res = []
            for element in partialcombo[i]:
                if element not in res:
                    res.append(element)
            partialcombo[i] = res
        return partialcombo[target]
