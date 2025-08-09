# Standard Set 1, Session 1
# Q4 ================================================================================================
''' Non-decreasing array
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example Output:

True
False
'''

def non_decreasing(nums):
    # keep track of how many times nums needs to be modified in order to be increasing
    # for loop: go through all array elements
        # if the number is smaller than the previous number, increase modification

    # if mod <= 1: return True else false
    
    modification = 0
    prev = nums[0]

    for num in nums:
        if num < prev:
            modification += 1
        prev = num

    if modification <= 1:
        return True
    
    return False

# Expecting
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))