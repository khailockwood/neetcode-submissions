class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for i in range(len(sandwiches)):
            if sandwiches[0] not in students:
                return len(students)
            else:
                students.pop(students.index(sandwiches[0]))
                sandwiches.pop(0)
        return 0
            

        