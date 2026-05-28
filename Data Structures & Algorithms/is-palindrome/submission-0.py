def is_alnum(char):
    if "A" <= char <= "Z":
        return chr(ord(char) + 32)
    elif "a" <= char <= "z" or "0" <= char <= "9":
        return char
    else:
        return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lst_s = []
        for i in range(0, len(list(s))):
            val = is_alnum(list(s)[i])
            if val:
                lst_s.append(val)
        len_lst_s = len(lst_s)
        for i in range(0,len(lst_s)):
            for j in range(len_lst_s-1, -1, -1):
                if lst_s[i] == lst_s[j]:
                    len_lst_s -= 1
                    break
                else:
                    
                    return False
        return True
