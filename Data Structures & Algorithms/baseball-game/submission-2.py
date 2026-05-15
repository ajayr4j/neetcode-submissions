class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in range(len(operations)):
            try:
                scores.append(int(operations[i]))
            except ValueError:
                if len(scores) >= 2:
                    if operations[i] == '+':
                        scores.append(scores[-1] + scores[-2])
                if len(scores) >= 1:
                    if operations[i] == 'D':
                        scores.append(scores[-1] * 2)
                    elif operations[i] == 'C':
                        scores.pop()
        return sum(scores)

