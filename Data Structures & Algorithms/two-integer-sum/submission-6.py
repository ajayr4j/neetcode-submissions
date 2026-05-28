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
        nums = [(value, index) for index, value in enumerate(nums)]
        nums = merge_sort(nums)

        hash_map = {}
        for num in nums:
            hash_map[num[0]] = num[1]

        for index, num in enumerate(nums):
            complement = target - num[0]
            if complement in hash_map and hash_map[complement] != num[1]:
                result = [num[1], hash_map[complement]]
                return [min(result), max(result)]
        
