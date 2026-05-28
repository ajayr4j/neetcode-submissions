def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    results = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1

    results.extend(left[i:])
    results.extend(right[j:])
    return results



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(val, original_index) for original_index, val in enumerate(nums)]
        nums = merge_sort(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
                
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                result = [nums[left][1], nums[right][1]]
                return [min(result), max(result)]