#!/usr/bin/python3
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list_number = []
        j = 0  
        while x != 0 : 
            value = x % 10
            print(f'value == {value}')
            list_number.append(value)  
            x = x // 10
            print(x)
        
        for i in reversed(range(0 , len(list_number)   )): 
            print(f'index is {i} and value is {list_number[i]}')
            print(f'index is {j} and value is {list_number[j]}')
            if list_number[j] != list_number[i]:
               return False
            else : 
                j += 1
        return True

solution = Solution()
print(solution.isPalindrome(-11))