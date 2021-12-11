# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
 def addOne(self, digits):
        length = len(digits)
        right =length-1
        carry =0
        for i in range(length-1, -1, -1):
            if i == right:
                current_value =digits[i]
                final = current_value+1
                if final ==10:
                    carry = 1
                    digits[i] =0
                else:
                    digits[i] =final
                    
            else:                
                current_value =digits[i]
                if carry ==1:
                    final = current_value+1
                else:
                    final = current_value 
                    
                if final ==10:
                    carry = 1
                    digits[i] =0
                else:
                    digits[i] =final
                    carry = 0
                    
            if i==0 and carry==1:
                digits= [1]+ digits
                        
                
        return digits
