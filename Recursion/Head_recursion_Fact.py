class Solution:
    def head(self, n):
        if n == 0:
            return

        self.head(n-1)

        print(n)


A = Solution()
print(A.head(5))

"""
Out -
1
2
3
4
5
None
"""
