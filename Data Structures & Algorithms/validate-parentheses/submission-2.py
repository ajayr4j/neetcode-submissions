class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        stack = []
        for s in s_list:
            if s in [')', '}', ']']:
                if not stack:
                    return False
                last_seen_bracket = stack.pop()
                if s == ')' and last_seen_bracket == '(':
                    continue
                elif s == '}' and last_seen_bracket == '{':
                    continue
                elif s == ']' and last_seen_bracket == '[':
                    continue
                else:
                    return False
            stack.append(s)
        if stack:
            return False
        else:
            return True


