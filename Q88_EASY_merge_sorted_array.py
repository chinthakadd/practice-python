from typing import List

# Intuition:
# Start from end. Keep winding backwards with two pointers at each array and another to fill num1 array in place
# Why start from end? If you start from beginning, you will have to keep a copy of num1 coz you need to do this in-place.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i = m - 1
        j = n - 1
        for k in range(len(nums1) - 1, -1, -1):
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
