class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        coursedict = {}
        for i in prerequisites:
            if i[0] not in coursedict:
                coursedict[i[0]] = [i[1]]
            else:
                coursedict[i[0]].append(i[1])

        coursepreq = {}
        for i in coursedict:
            coursepreq[i] = coursedict[i]
        emptychecker = False
        while emptychecker == False:
            for course in coursepreq:
                prereq = set()
                for item in coursepreq[course]:
                    if item in coursedict:
                        for item2 in coursedict[item]:
                            if item2 == course:
                                return False
                            prereq.add(item2)
                coursepreq[course] = list(prereq)
            for course in coursepreq:
                emptychecker = True
                if coursepreq[course] != []:
                    emptychecker = False
        return True
