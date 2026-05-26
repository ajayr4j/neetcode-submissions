class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_list = []

        for index1, i in enumerate(nums):
            new_val = 1
            for index2, j in enumerate(nums):
                if index1 == index2:
                    continue
                else:
                    new_val *= j
            ans_list.append(new_val)
        return ans_list