from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        for sandwich in sandwiches:
            rotations = 0
            while queue[0] != sandwich:  
                queue.append(queue.popleft())
                rotations += 1
                if rotations == len(queue):
                    return len(queue)
            queue.popleft()
        return len(queue)