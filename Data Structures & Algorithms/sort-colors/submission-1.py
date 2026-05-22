class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1

        colors = []
        for index, count in enumerate(counts):
            for c in range(count):
                colors.append(index)

        nums[:] = colors