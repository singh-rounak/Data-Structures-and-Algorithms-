class Solution(object):
  def containsDuplicate(self, nums):
    Hmap = {}
    for num in nums:
        if num not in Hmap:
            Hmap[num] = 1
        else:
            Hmap[num] += 1

    for key in Hmap.keys():
        if Hmap[key] >1:
            return True
    return False
      
      
