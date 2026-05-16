class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in [')', '}', ']']:
                if not stack:
                    return False
                last_seen_bracket = stack.pop()
                if ch == ')' and last_seen_bracket == '(':
                    continue
                elif ch == '}' and last_seen_bracket == '{':
                    continue
                elif ch == ']' and last_seen_bracket == '[':
                    continue
                else:
                    return False
            stack.append(ch)
        if stack:
            return False
        else:
            return True


