class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if (((nums[i] + nums[j]) == target) and (i != j)):
                    return (i, j)
                
nums1, nums2, nums3 = [2,7,11,15], [3,2,4], [3,3]
target1, target2, target3 = 9, 6, 6

s1 = Solution()
print(s1.twoSum(nums1, target1))
print(s1.twoSum(nums2, target2))
print(s1.twoSum(nums3, target3))