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