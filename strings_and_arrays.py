# Advanced Set 1, Session 1
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

# Q7 
''' Problem 7: Eeyore's House
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1.

Example Output:
5
2
'''

def good_pairs(pile1, pile2, k):
	pass


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)

# Q8
''' Problem 8: Defuse the Bomb
Batman has a bomb to defuse, and his time is running out! His butler, Alfred, is on the phone providing him with a circular array code of length n and key k.

To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!

Example Output:

[12, 10, 16, 13]
[0, 0, 0, 0]
[12, 5, 6, 13]
'''

def defuse(code, k):
	# extend the code array twice > just duplicate the values

    # for loop: access the first n elements
        # if: to check k to perform teh proper changes

    # return the first n valus of code

    n = len(code)

    code = code * 2

    for i in range(n):
        if k > 0:
            sum = 0
            for value in code[i + 1:i + k + 1]:
                sum += value
            code[i] = sum
        if k < 0:
            sum = 0
            for value in code[i + n + k:i + n]:
                sum += value
            code[i] = sum
        if k == 0:
            code[i] = 0

    return code[:n]


code = [5, 7, 1, 4]
k = 3
print(defuse(code, k))

code = [1, 2, 3, 4]
k = 0
print(defuse(code, k))

code = [2, 4, 9, 3]
k = -2
print(defuse(code, k))