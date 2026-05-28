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
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    results.extend(left[i:])
    results.extend(right[j:])
    return results

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = merge_sort(nums)
        ans_list = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:  
                continue
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > -a:
                    right -= 1
                elif nums[left] + nums[right] < -a:
                    left += 1
                else:
                    ans_list.append([a, nums[left], nums[right]])
                    left += 1 
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
        return ans_list
