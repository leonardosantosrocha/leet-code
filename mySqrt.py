class Solution:
    def mySqrt(self, x : int) -> int:
        i = 1

        while ((i * i) <= x):
            i += 1
        return i - 1
        

x1, x2, x3 = 4, 7, 9

s1 = Solution()
print(s1.mySqrt(x1))
print(s1.mySqrt(x2))
print(s1.mySqrt(x3))