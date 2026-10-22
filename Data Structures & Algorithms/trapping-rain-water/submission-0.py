class Solution(object):
    def trap(self, height):
        left_pointer = 0               #set a pointers
        right_pointer = len(height) - 1
        left_max = 0#height of the left bar is filhal is 0
        right_max = 0#height of the right bar is filhal is 0
        total_water = 0 

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                if height[left_pointer] >= left_max:
                    left_max = height[left_pointer]
                else:
                    total_water += left_max - height[left_pointer]

                left_pointer += 1

            else:
                if height[right_pointer] >= right_max:
                    right_max = height[right_pointer]

                else:
                    total_water += right_max - height[right_pointer]

                right_pointer -= 1

        return total_water
