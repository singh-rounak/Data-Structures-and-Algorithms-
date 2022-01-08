class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!= i:
                return i
        return len(nums)
    
    #O(n) Linear Time
    #O(1) Constant Space

'''
Driver Code:
Object = Solution()		#Instantiation
A  = INPUT
print(Object.missingNumber(A))

1. [3,0,1]
OUTPUT- 2
[Finished in 0.4s]

2) [1,1]
OUTPUT- 0
[Finished in 3.4s]
'''
