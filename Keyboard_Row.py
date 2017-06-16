class Solution(object):
    def findWords(self, words):
    	a=set('qwertyuiop')
    	b=set('asdfghjkl')
    	c=set('zxcvbnm')
    	ans=[]
    	for word in words:
    		t=set(word.lower())
    		if a&t==t:
    			ans.append(word)
    		if b&t==t:
    			ans.append(word)
    		if c&t==t:
    			ans.append(word)
    	return ans
    	# keyboard={'1':['q','w','e','r','t','y','u','i','o','p'],'2':['a','s','d','f','g','h','j','k','l'],'3':['z','x','c','v','b','n','m']}
    	# dic={}
    	# ans1=[]
    	# l=['q','w','e','r','t','y','u','i','o','p']
    	# l1=['a','s','d','f','g','h','j','k','l']
    	# l2 = ['z','x','c','v','b','n','m']
    	# for i in l:
    	# 	dic[i]=1 
    	# for i in l1:
    	# 	dic[i]=2
    	# for i in l2:
    	# 	dic[i]=3
    	# for word in words:
    	# 	wd =list(word.lower())
    	# 	while(len(set([dic[i] for i in wd[::]]))==1):
    	# 		ans1.append(word)
    	# return ans1
    	# for k in words:
    	# 	ans= True
    	# 	wd = list(k)
    	# 	for i in range(0,len(wd)-1):
    	# 		if dic[wd[i].lower()]==dic[wd[i+1].lower()]:
    	# 			ans=True
    	# 		else: ans = False
    	# 	while(ans==True):
    	# 		ans1.append(k)

    	# return ans1


if __name__=='__main__':
	words = ["Hello", "Alaska", "Dad", "Peace"]
	ans = Solution()
	print(ans.findWords(words))