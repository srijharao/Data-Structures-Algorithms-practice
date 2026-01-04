'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in range(len(digits)-1,-1,-1):
            num_sum = digits[i] + carry
            carry = num_sum // 10
            num_sum = num_sum % 10
            digits[i] = num_sum
        
        if carry > 0:
            result = []
            result.append(carry)
            result.extend(digits)
            return result
        
        else:
            return digits


        #O(N), O(N)
