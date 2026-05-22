class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_rows = len(matrix)
        top = 0
        bot = len_rows - 1
        nums = None

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                nums = matrix[row]
                break
                
        if nums is None:
            return False
        
        
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

        

            