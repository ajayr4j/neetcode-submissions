class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [item for sublist in matrix for item in sublist]
        l = 0
        h = len(nums) - 1
        while l <= h:
            m = (l + h)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                h = m - 1
            else:
                return True
        return False
