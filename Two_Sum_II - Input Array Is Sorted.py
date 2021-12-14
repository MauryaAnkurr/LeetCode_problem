#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
#Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low_index = 0
        high_index = len(numbers)-1
        
        while True:
            sums = numbers[low_index] + numbers[high_index]
            if sums < target:
                low_index += 1
            elif sums > target:
                high_index -= 1
            else:
                return [low_index+1, high_index+1]
