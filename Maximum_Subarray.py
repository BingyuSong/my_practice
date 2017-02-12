class Solution(object):
    def maxSubArray(self, nums):

#前面的最大和加上当前值若小于当前值，则保留当前值放弃了前面的序列
#最大值为前面的最大和，或当前最大值。因为最大子序列可以是一个数。   	
    	if len(nums)==1:	
    		return nums[0]
    	else:
        	sumNum = nums[0]
        	maxNum = sumNum
        	for i in range(1, len(nums)):
        		print(nums[i])
        		sumNum = max(sumNum+nums[i],nums[i])
        		maxNum = max(maxNum, sumNum)
        	return maxNum

if __name__=='__main__':
	ans = Solution()
	print(ans.maxSubArray([1,2]))