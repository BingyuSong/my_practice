class Solution(object):
    def findRestaurant(self, list1, list2):
    	com=[i for i in list1 if i in list2]
    	index, dic=[],{}
    	for j in com:
    		index.append(list1.index(j)+list2.index(j))
    	for i in range(0,len(index)):
    		if index[i] in dic.keys():
    			dic[index[i]].append(com[i])
    		else:
    			dic[index[i]]=[com[i]]
    	return dic[min(index)]


if __name__=='__main__':
	ans=Solution()
	list1=["Shogun","Tapioca Express","Burger King","KFC"]
	list2=["KFC","Burger King","Tapioca Express","Shogun"]
	print(ans.findRestaurant(list1,list2))
    	
