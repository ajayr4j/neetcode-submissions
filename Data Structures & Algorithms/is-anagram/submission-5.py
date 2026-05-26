class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}

        for index, i in enumerate(list(s)):
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for index, i in enumerate(list(t)):
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        keys_to_remove = []
        for key in s_dict.keys():
            if key not in t_dict:
                return False
            if s_dict[key] == t_dict[key]:
                keys_to_remove.append(key)
                continue
            else:
                return False

        for key in keys_to_remove:
            s_dict.pop(key)
            t_dict.pop(key)
        
        if not s_dict and not t_dict:
            return True
        else:
            return False
        
