class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mult_ord_lst = []
        for str1 in strs:
            print(list(str1))
            mult_ord = 1
            for i in list(str1):
                mult_ord *= ord(i)
            mult_ord_lst.append(mult_ord)
        
        mult_ord_dict = {}
        for index, mult_ord in enumerate(mult_ord_lst):
            if mult_ord in mult_ord_dict:
                mult_ord_dict[mult_ord].append(strs[index])
            else:
                mult_ord_dict[mult_ord] = [strs[index]]
        return (list((mult_ord_dict.values())))