class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = [1] * n 
        #step 1: calculate PREfix
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix = prefix * nums[i]
        # STEP 2: Calculate SUFFIX products
        suffix = 1

        for i in range(n - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]

        return output
        




        