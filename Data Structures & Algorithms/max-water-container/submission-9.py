class Solution:
    def maxArea(self, heights: List[int]) -> int:
        widths = []
        water_capacity = {}
        for i, height1 in enumerate(heights):
            for j, height2 in enumerate(heights):
                width = abs(j-i)
                min_height = min(height1, height2)
                water_capacity[(i,j)] = (min_height * width,width)
                # print(height1, height2, width, water_capacity[(i,j)][0])
        r_sorted = dict(sorted(water_capacity.items(), key=lambda item:  item[1][0], reverse=True))
        (left, right) = next(iter(r_sorted.keys()))
        return min(heights[left], heights[right]) * r_sorted[(left, right)][1]