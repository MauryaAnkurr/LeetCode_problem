#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
#representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order. 
def merge(self, nums1, m, nums2, n):
      """
      :type nums1: List[int]
      :type m: int
      :type nums2: List[int]
      :type n: int
      :rtype: None Do not return anything, modify nums1 in-place instead.
      """
      nums1_copy =nums1[:m]

      p1 =0
      p2=0

      for p in range(n+m):
          if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
              nums1[p] = nums1_copy[p1] 
              p1 += 1
          else:
              nums1[p] = nums2[p2]
              p2 += 1
