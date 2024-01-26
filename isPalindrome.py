class Solution:
    def isPalindrome(self, x : int) -> bool:
        x = str(x)
        a = [x[i] for i in range(0, len(x), 1)]
        b = [x[j] for j in range(len(x)-1, -1, -1)]

        if (a != b):
            return False
        else: 
            return True
        
x1, x2, x3 =  121, -121, 10

s1 = Solution()
print(s1.isPalindrome(x1))
print(s1.isPalindrome(x2))
print(s1.isPalindrome(x3))