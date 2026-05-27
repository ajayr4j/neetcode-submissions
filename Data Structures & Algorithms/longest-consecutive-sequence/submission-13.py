def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = merge_sort(nums)
        if len(nums) > 0:
            diff_list = [1]
        else:
            diff_list = []

        for index, num in enumerate(nums):
            if index != 0:
                diff_list.append(nums[index] - nums[index - 1])
        print(nums)
        print(diff_list)
        current = 1
        longest = 1

        if len(nums) == 0:
            return 0
        for diff in diff_list[1:]:
            if diff == 1:
                current += 1
                longest = max(longest, current)
            elif diff == 0:
                pass         
            else:
                current = 1  
        return longest
