class Solution(object):
    def subsetsWithDup(self, nums):

        res = []
        nums.sort()

        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)


A = Solution()
b = [1, 2, 2, 5]
print(A.subsetsWithDup(b))
