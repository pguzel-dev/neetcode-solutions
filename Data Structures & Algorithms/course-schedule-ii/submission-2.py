# V = numCourses
# E = number of prerequisite pairs

# Time: O(V + E)
# Space: O(V + E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        cycle = set()
        visited = set()
        result = []

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)

            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result