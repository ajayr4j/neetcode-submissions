class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        for i in range(len(s)):
            seen = set()
            current = 0
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    current += 1
                else:
                    break
            longest = max(longest, current)
        
        return longest