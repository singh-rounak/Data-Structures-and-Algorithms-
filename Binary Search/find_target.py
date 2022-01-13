class solution:
  def find_target(self, nums, target):
    
    for ind, num in enumerate(nums):
        if num == target:
            return ind
    return -1
    
Object = Solution()
print(Object.find_target([1,4,7,5,9,8,7,3,5], 9))

"""
OUT 4
[Finished in 0.3s]

Time: O(logn)
Space:O(1)
"""
