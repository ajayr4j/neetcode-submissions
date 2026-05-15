class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_list = []
        for index in range(len(arr)):
            if index + 1 == len(arr):
                new_list.append(-1)
            else:
                new_list.append(max(arr[index+1:]))
        return new_list
