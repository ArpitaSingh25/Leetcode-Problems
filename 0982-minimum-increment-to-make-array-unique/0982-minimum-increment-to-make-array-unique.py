class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                moves += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return moves

# Example usage:
sol = Solution()
print(sol.minIncrementForUnique([1, 2, 2])) # Output: 1
print(sol.minIncrementForUnique([3, 2, 1, 2, 1, 7])) # Output: 6
