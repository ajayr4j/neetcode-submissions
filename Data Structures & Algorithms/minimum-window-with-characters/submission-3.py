def get_hash_map(arr):
    hash_map = {}
    for index, val in enumerate(arr):
        if val in hash_map:
            hash_map[val] += 1
        else:
            hash_map[val] = 1
    return hash_map

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_lst = list(t)
        s_lst = list(s)
        hash_map = get_hash_map(t_lst)
        print(hash_map)
        starting_indices = []

        for index, val in enumerate(s_lst):
            if val in hash_map:
                starting_indices.append(index)
        
        results = []
        for start_index in starting_indices:
            hash_map_temp = hash_map.copy()
            result = []
            for i in range(start_index, len(s_lst)):
                if s_lst[i] in hash_map_temp and hash_map_temp[s_lst[i]] > 0:
                    hash_map_temp[s_lst[i]] -= 1
                result.append(s_lst[i])
                if sum(hash_map_temp.values()) == 0:
                    break
            if sum(hash_map_temp.values()) == 0:
                results.append("".join(result))

        results.sort(key=lambda x: len(x))
        print(results)
        return results[0] if results else ""
