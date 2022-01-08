
class Solution(object):
	def singleNumber(self, nums):
		Hmap = {}

		for num in nums:
			if num not in Hmap:
				Hmap[num]  = 1
			else:
				Hmap[num] += 1
		for key in Hmap.keys():
			if Hmap[key] ==1:
				return key

nums = [4,1,2,1,2]

Object = Solution()
print(Object.singleNumber(nums))



"""
In - [4,1,2,1,2]
Out - 4
[Finished in 0.2s]

Linear Time. O(n)
Linear Space O(n)

"""
