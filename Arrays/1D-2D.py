class Solution(object):
	def construct2DArray(self, original, m, n):
		size = m*n

		if size != len(original):
			return None

		if m==1:
			return [original]

		return[original[i:i+n] for i in range(0,len(original), n)]

Object = Solution()
print(Object.construct2DArray(original, 2,2))

