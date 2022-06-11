class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in points:
            distance.append(sqrt(i[0]**2+i[1]**2))
        distance2 = deepcopy(distance)
        distance2.sort()
        maxd = distance2[k-1]
        solution = []
        j=0
        while j < len(points):
            if distance[j] <= maxd:
                solution.append(points[j])
            j+=1
        return solution
        
