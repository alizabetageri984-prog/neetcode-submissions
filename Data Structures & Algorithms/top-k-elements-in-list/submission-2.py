class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

         # Step 1: Count frequency
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            # Step 2: Sort by frequency
        result = sorted(count, key=count.get, reverse = True)
            # Step 3: Return top k
        return result[:k]