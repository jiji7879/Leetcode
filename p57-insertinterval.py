#brute forced
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        imin = 0
        imax = 0
        for i in intervals:
            if i[0] < newInterval[0]:
                imin += 1
            if i[0] <= newInterval[1]:
                imax += 1
            if i[1] < newInterval[0]:
                imin += 1
            if i[1] <= newInterval[1]:
                imax += 1
            else:
                break
        print(imin)
        print(imax)
        if imin % 2 == 1:
            if imax % 2 == 0:
                j = imin // 2
                intervals.insert(j, [intervals[j][0], newInterval[1]])
                k = imax // 2
                while k >= j+1:
                    del intervals[j+1]
                    k -= 1
            else:
            #elif imax % 2 == 1:
                j = imin // 2
                k = imax // 2
                intervals[j] = [intervals[j][0], intervals[k][1]]
                while k >= j+1:
                    del intervals[j+1]
                    k -= 1
        else:
        #elif imin % 2 == 1:
            if imax % 2 == 0:
                j = imin // 2
                k = imax // 2
                intervals.insert(j, newInterval)
                while k >= j+1:
                    del intervals[j+1]
                    k -= 1
            else:
            #elif imax % 2 == 1:
                j = imin // 2
                k = imax // 2
                intervals[j] = [newInterval[0], intervals[k][1]]
                while k >= j+1:
                    del intervals[j+1]
                    k -= 1
        return intervals
