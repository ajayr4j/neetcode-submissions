class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_dict = {}
        for index, i in enumerate(nums):
            if i in ans_dict:
                ans_dict[i] += 1
            else:
                ans_dict[i] = 1

        ans_dict = dict(sorted(ans_dict.items(), key=lambda item: item[1], reverse=True))
        print(ans_dict)
        lst_1 = []

        for key in ans_dict.keys():
            if len(lst_1) == k:
                return lst_1
            else:
                lst_1.append(key)
        return lst_1