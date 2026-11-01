
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        while left <= right:

            mid1 = (left + right) // 2
            mid2 = (m + n + 1) // 2 - mid1

            # Find left and right elements of both arrays
            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            r1 = float('inf') if mid1 == m else nums1[mid1]

            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == n else nums2[mid2]

            # Correct partition found
            if l1 <= r2 and l2 <= r1:

                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2

                else:
                    return float(max(l1, l2))

            # Move binary search towards the left
            elif l1 > r2:
                right = mid1 - 1

            # Move binary search towards the right
            else:
                left = mid1 + 1

        return 0.0

        