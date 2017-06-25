class Solution(object):
    def titleToNumber(self, s):
    	s=s[::-1]
    	sum=0
    	# enumerate 函数可以直接获取index和对应的值
    	for index,char in enumerate(s):
    		sum+=(ord(char)-65+1)*(26**index)
    	return sum

if __name__=='__main__':
	ans=Solution()
	print(ans.titleToNumber('BA'))