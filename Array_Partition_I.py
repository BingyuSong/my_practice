class Solution(object):
    def arrayPairSum(self, nums):
    	# nums.sort()
    	# ans = 0
    	# i=0
    	# while(i<len(nums)):
    	# 	ans+= nums[i]
    	# 	i+=2
    	# return ans
    	return sum(sorted(nums)[::2])

if __name__=='__main__':
	a = Solution()
	nums = [1,4,3,2]
	print(a.arrayPairSum(nums))