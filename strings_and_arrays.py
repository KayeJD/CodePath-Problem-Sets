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


# Q5
''' Problem 5: Missing Clues
Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

Example Output:

[[2, 2], [4, 49], [51, 74], [76, 99]]
[]
'''

def find_missing_clues(clues, lower, upper):
   pass

# Example Usage:

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

clues = [-1]
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)


# Q6
''' Problem 6: Vegetable Harvest
Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that are ready to harvest in the vegetable patch. A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.

Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.

Example Output: 6
'''

def harvest(vegetable_patch):
	# nested for loop to check each char value
    # return count of char == 'c'

    count = 0

    for row in vegetable_patch:
        for char in row:
            if char == 'c':
                count += 1

    return count

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]

print(harvest(vegetable_patch))