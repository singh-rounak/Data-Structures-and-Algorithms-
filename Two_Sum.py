class Solution(object):
  
  def twosum(self, nums, target):
    
    Hamp = {}
    
    for i in range(len(nums)):
      if target - nums[i] in Hmap:
        return[Hmap[target - nums[i]], i]
       else:
        Hmap[nums[i]] = i
