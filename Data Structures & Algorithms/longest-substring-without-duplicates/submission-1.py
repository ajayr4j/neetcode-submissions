class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        seen = set()
        longest = 0
        
        for R in range(len(s)):
            if s[R] not in seen:
                seen.add(s[R])
                longest = max(len(seen), longest)
            else:
                while s[R] in seen:
                    seen.remove(s[L])
                    L += 1
                seen.add(s[R])
        return longest