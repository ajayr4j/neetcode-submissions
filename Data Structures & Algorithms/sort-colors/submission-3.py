class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0

        for num in nums:
            if num == 0:
                a += 1
            elif num == 1:
                b += 1
            else:
                c += 1


        colors = []
        for _ in range(a):
            colors.append(0)
        for _ in range(b):
            colors.append(1)
        for _ in range(c):
            colors.append(2)
    
        nums[:] = colors