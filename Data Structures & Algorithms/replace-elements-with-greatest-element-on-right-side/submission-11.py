class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_list = []
        max_list = []
        for index in range(len(arr)-1, 0, -1):
            max_list.append((arr[index]))
            if index != 0:
                new_list.append(max(max_list))
        new_list.reverse()
        new_list.append(-1)
        return new_list
