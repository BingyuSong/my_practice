class Solution(object):
    def reverseWords(self, s):
    	ls = s.split(' ')
    	for i in range(0,len(ls)):
    		ls[i]=ls[i][::-1]
    	return ' '.join(ls)


if __name__=='__main__':
	ans = Solution()
	s="Let's take LeetCode contest"
	print(ans.reverseWords(s))