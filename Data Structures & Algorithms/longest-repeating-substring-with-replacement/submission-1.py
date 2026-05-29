def get_hash_map(arr):
    hash_map = {}
    for index, val in enumerate(arr):
        if val in hash_map:
            hash_map[val] += 1
        else:
            hash_map[val] = 1
    return hash_map

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        L = 0
        hash_map = {}

        for R in range(len(s)):
            hash_map[s[R]] = hash_map.get(s[R], 0) + 1

            hash_map_sum = sum(hash_map.values())
            hash_map_max = max(hash_map.values())
            if not hash_map_sum - hash_map_max <= k:
                hash_map[s[L]] -= 1
                L += 1
            else:
                longest = max(hash_map_sum, longest)
        return longest