class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:        # cleaner than range(len(...))
            try:
                scores.append(int(op))
            except ValueError:
                if op == '+':
                    scores.append(scores[-1] + scores[-2])
                elif op == 'D':
                    scores.append(scores[-1] * 2)
                elif op == 'C':
                    scores.pop()
        return sum(scores)