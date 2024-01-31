class Solution:
    def toLowerCase(self, s : str) -> str:
        return s.lower()

x1, x2, x3 = "Hello", "here", "LOVELY"

s1 = Solution()
print(s1.toLowerCase(x1))
print(s1.toLowerCase(x2))
print(s1.toLowerCase(x3))