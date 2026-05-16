class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in pairs:               # it's a closing bracket
                if not stack:
                    return False
                if stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)          # it's an opening bracket
        return not stack