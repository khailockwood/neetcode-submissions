class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visited = set()
        visiting = set()

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in adjList:
                adjList[prerequisites[i][0]] = [prerequisites[i][1]]
            else:
                adjList[prerequisites[i][0]].append(prerequisites[i][1])
        
        print(adjList)
  

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True

            visiting.add(node)

            for neighbor in adjList.get(node,[]):
                res = dfs(neighbor);
                if not res:
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True

        for i in range(numCourses):
            res = dfs(i)
            print(res)
            if not res:
                return False
        return True


