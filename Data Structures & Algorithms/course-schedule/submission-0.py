class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to the list of courses it depends on
        preMap = { i:[] for i in range(numCourses)}

        # Build prerequisite list for each course
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # visited stores courses in the current DFS path
        # If we see the same course again, there is a cycle
        visited = set()

        def dfs(course):
            # Cycle detected
            if course in visited:
                return False

            # No prerequisites left, so this course is safe
            if preMap[course] == []:
                return True
            
            # Mark course as part of current DFS path
            visited.add(course)

            # Check every prerequisite first
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            # Remove course after finishing this path
            visited.remove(course)

            # Cache result: this course has no cycle
            preMap[course] = []

            return True
        
        # Try starting DFS from every course
        for course in range(numCourses):
            if not dfs(course):
                return False

        # All courses can be completed
        return True