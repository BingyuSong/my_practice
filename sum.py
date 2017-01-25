class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		carry = 0
		root = n =ListNode(0)
		while l1 or l2 or carry:
			v1 = v2 = 0
			if l1:
				v1 = l1.val
				l1 = l1.next
			if l2:
				v2 = l2.val
				l2 = l2.next
			carry, val = divmod(v1+v2+carry,10)
			n.next = ListNode(val)
			n = n.next
		return root.next

		

		
	
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next =  node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

l1 = node1
l2 = node4
s = Solution()
ans = s.addTwoNumbers(l1,l2)
print(ans.next.val)

