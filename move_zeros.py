#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.
def moveZeroes(self, nums):
        index =0
        
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index = index+1
        
        for i in range(index,len(nums)):
            nums[i]=0
        return nums
