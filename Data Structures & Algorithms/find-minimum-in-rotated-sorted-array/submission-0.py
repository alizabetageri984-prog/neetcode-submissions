class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer= len(nums) - 1


        while left_pointer < right_pointer :
            middle_pointer = (left_pointer + right_pointer) // 2

            if nums[middle_pointer] > nums[right_pointer]:
                left_pointer = middle_pointer + 1

            elif nums[middle_pointer] < nums[right_pointer]:
                right_pointer = middle_pointer 

            else:
                right_pointer -= 1

        return nums[left_pointer]
        