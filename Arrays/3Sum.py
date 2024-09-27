Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

#Make Sure to not have duplicates: -> sort
nums.sort()
res = []

for index, num in nums:
    if index > 0 and num == nums[index -1]:
    
    left = index+1
    right = len(nums) -1
    
    while left < right:
        curr = num + nums[left] + nums[right] 
        if curr > 0:
            right -= 1
        elif curr < 0:
            left += 1
        else:
            res.append([num, nums[left], nums[right]])
            
            left += 1
            while nums[left] == nums[left -1] and left < right:
                left+=1
                
    return res

    #Time: O(n.n)
    #Space: O(n)