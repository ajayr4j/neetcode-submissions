class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_list = []
        count  = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            count_list.append(count)

        return max(count_list)