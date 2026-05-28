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
    def maxProfit(self, prices: List[int]) -> int:
        pnl_lst = [0]
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    pnl_lst.append(prices[j] - prices[i])

        return merge_sort(pnl_lst)[-1]