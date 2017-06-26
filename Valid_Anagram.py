from collections import *

class Solution(object):
    def isAnagram(self, s, t):
        if s==t: return True
    	d1=Counter(s)
    	d2=Counter(t)
    	mask=True
    	if d1.keys() != d2.keys(): return False
    	for i in d1.keys():
    		if d1[i] != d2[i]: mask=False
    	return mask

