

""" Tail Recursion with saved result - Only one function present in stack for every recursive call [GOOD SOLUTION] """


class Solution:
    def fact(self, n, result):

        if n == 1:
            return result

        return self.fact(n-1, n*result)


A = Solution()
print("____________")
print(A.fact(5, 1))
print("____________")


""" Tail Recursion with unknown varibale - function calls pile up in stack with every recursive call [NOT A GOOD SOLUTION]"""
# class Solution:
#     def fact(self, n):

#         if n == 1:
#             return 1

#         return n * self.fact(n-1)


# A = Solution()
# print("____________")
# print(A.fact(5))
# print("____________")

"""
Out - 
____________
120
____________

"""
