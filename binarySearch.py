class Solution:
    def search(self, nums : list, target : int) -> int:
        left = 0 
        right = len(nums) - 1
        
        while (left <= right):
            middle = int((left + right) / 2)
            if (nums[middle] < target):
                left = middle + 1
            elif (nums[middle] > target):
                right = middle - 1
            else:
                return middle
        return -1

x1, x2, x3 = [-1,0,3,5,9,12], [-1,0,3,5,9,12], []

s1 = Solution()
print(s1.binarySearch(x1, 9))
print(s1.binarySearch(x2, 2))
print(s1.binarySearch(x3, 1))