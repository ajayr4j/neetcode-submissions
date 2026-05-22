class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        len_nums = len(nums)
        h = len_nums
        while l <= h:
            m = (l + h)//2
            if m > len_nums - 1:
                break
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                h = m - 1
            else:
                return m
        return -1

