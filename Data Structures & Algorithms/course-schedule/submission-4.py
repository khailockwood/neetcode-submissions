class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        visiting = set()
        
        for i in range(len(prerequisites)):
            if prerequisites[i][0] in adjList:
                adjList[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                adjList[prerequisites[i][0]] = [prerequisites[i][1]]
            
        print(adjList)

        #now have adjList mapping each course to it's prereq

        def dfs(course):
            if course in visiting: #if we hit a cycle, return False
                return False
            
            if adjList.get(course, []) == []: #if no prereqs for this course
                return True
            
            visiting.add(course)
            for prereq in adjList.get(course, []): #for all prereqs for this course
                if not dfs(prereq): #go down the path
                    return False
            
            visiting.remove(course)
            adjList[course] = []
            return True

            
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            


            