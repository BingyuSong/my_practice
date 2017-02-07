class Solution(object):
    def removeElement(self, nums, val):
    	index = 0
    	count = 0
    	for flag in nums:
    		if flag != val:
    			nums[index]=flag
    			index+=1
    			count+=1
    	print(nums)
    	return count

if __name__=='__main__':
	ans = Solution()
	print(ans.removeElement([1,3,4,5],4))
