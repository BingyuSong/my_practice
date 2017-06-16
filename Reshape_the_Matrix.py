class Solution(object):
    def matrixReshape(self, nums, r, c):
    	try:
    		return np.reshape(nums, (r, c)).tolist()
    	except:
    		return nums


if __name__=='__main__':
	nums=[[1,3],[2,4]]
	ans = Solution()

	print(ans.matrixReshape(nums,1,4))
