"""
Problem: Two Sum
Difficulty: Easy
Topic: Arrays, Hash Map

Summar
Eng: Given a list of integers and a target number, return the indices of the two
numbers that add up to the target.
Esp: Dado una lista de enteros y un número objetivo, devuelve los índices de los dos
números que suman el objetivo.

Important:
- Return indices, not the numbers.
- Each inpuit has exactly one valid solution.
- The same element cannot be used twice.

Example:
Input: nums = [2, 7, 11, 15]
target = 9

Output: [0, 1]

Reason:
nums[0] + nums[1] = 2 + 7 = 9

Approach:

Instead of checking every possible pair with two loops, we use a dicctionary
to store the numbers we have already seen and their indices. For each number, we calculate its complement

For each number:
1. Calculate the complement needed to reach the target.
2. Check if the complement already exists in the dictionary.
3. If it exists, return the indix of the complement and the current index.
4. If it does not exist, store the current number and its index.

Complexity:

Time: O(n) 
Space: O(n) 
"""



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, number in enumerate(nums):
            complement = target - number
            
            if complement in seen:
                return [seen[complement], index]
            
            seen[number] = index

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]