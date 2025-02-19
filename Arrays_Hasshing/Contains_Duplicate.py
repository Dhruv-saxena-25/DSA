"""
* Contains Duplicate
    -- Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""

## Hash Set
def hasDuplicate(nums):
    unique_nums= set()
    for num in nums:
        if num in unique_nums:
            return True
        unique_nums.add(num)
    return False
print(hasDuplicate([1, 2, 3, 4, 4]))
    
'''
## Follow-Up Questions
1) Is Anagram
2) Two Integer Sum 
'''

