class Solution(object):
    def nextGreaterElement(self, findNums, nums):
#如果栈为空，放入第一个数
#如果后一个数比当前数大，从栈中取出（pop）当前数，建立当前数与下一个的dict，在将下一个数放入栈中
#如果后一个数不比当前数大，则将下一个数直接放入栈中
#直至所以数都被匹配成功
    	dic={}
    	stc=[]
    	for i in nums:
    		while stc and stc[-1]<i:
    			dic[stc.pop()]=i
    		stc.append(i)
    	return [dic.get(n,-1) for n in findNums]

if __name__=='__main__':
	ans = Solution()
	findNums=[4,1,2]
	nums=[1,3,4,2]
	print(ans.nextGreaterElement(findNums,nums))



