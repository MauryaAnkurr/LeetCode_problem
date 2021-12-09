#Remove elements
#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
 def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        length = len(nums)
        i=0
        for j in range(length):
            if nums[j]!=val:               
                nums[i]=nums[j]
                i = i+1
           
        return i     
        
