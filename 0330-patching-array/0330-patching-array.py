class Solution:
    @staticmethod
    def minPatches(nums, n):
        patches = 0
        miss = 1
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1

        return patches

# Example usage:
nums1 = [1, 3]
n1 = 6
print(Solution.minPatches(nums1, n1))  # Output: 1

nums2 = [1, 5, 10]
n2 = 20
print(Solution.minPatches(nums2, n2))  # Output: 2

nums3 = [1, 2, 2]
n3 = 5
print(Solution.minPatches(nums3, n3))  # Output: 0
