# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = []
        m = head
        while m != None:
        	temp.append(m.val)
        	m=m.next
        print(temp)
        if n==0:
        	return head
        else:
        	del(temp[-n])
        newhead = head
        newhead.val = temp[0]
        s = newhead
        for i in range(1,len(temp)):
        	key = ListNode(temp[i])
        	#key.val = temp[i]
        	s.next = key
        	s = key
        return newhead
s =Solution()
k = ListNode(1)
l = ListNode(2)
w = ListNode(3)
k.next = l
l.next = w
ans = s.removeNthFromEnd(k,1)
print(ans.val)
print(ans.next.val)







        