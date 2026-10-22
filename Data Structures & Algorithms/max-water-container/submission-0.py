class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_water = 0

        while left_pointer < right_pointer:
            current = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer +=1
            else:
                right_pointer -= 1
            if max_water < current:
                max_water = current

        return max_water
        


        