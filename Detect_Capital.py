class Solution(object):
    def detectCapitalUse(self, word):
    	if word.lower()==word or word.upper()==word or word[0].lower()+word[1:]==word.lower(): return True
    	else: return False

if __name__=='__main__':
	ans=Solution()
	print(ans.detectCapitalUse('Leetcode'))