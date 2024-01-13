#!/usr/bin/python3
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store elements and their indices
        num_dict = {}

        # Loop through the array
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
            print(f'{num_dict}')

        # If no solution is found, return an empty list
        return []
    
solution = Solution()
print(solution.twoSum([2, 7, 11, 5 , 0], 5))