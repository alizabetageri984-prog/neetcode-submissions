class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left_pointer = i + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                total = nums[i] + nums[left_pointer] + nums[right_pointer]

                if total == 0:
                    result.append(
                        [nums[i], nums[left_pointer], nums[right_pointer]]
                    )

                    left_pointer += 1
                    right_pointer -= 1

                    # Skip duplicate values
                    while (
                        left_pointer < right_pointer
                        and nums[left_pointer] == nums[left_pointer - 1]
                    ):
                        left_pointer += 1

                    while (
                        left_pointer < right_pointer
                        and nums[right_pointer] == nums[right_pointer + 1]
                    ):
                        right_pointer -= 1

                elif total < 0:
                    left_pointer += 1

                else:
                    right_pointer -= 1

        return result
        