class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, i in enumerate(nums):
            for index2, j in enumerate(nums):
                if index1 != index2:
                    if i + j == target:
                        return [index1, index2]