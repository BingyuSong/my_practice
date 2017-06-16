class Solution(object):
    def fizzBuzz(self, n):
    	ans = [str(i) for i in range(1,n+1)]
    	three=[int(x) for x in ans if int(x)%3==0 and int(x)%15 != 0]
    	five = [int(x) for x in ans if int(x)%5==0 and int(x)%15 != 0]
    	fif = [int(x) for x in ans if int(x)%15==0]
    	for i in three : ans[i-1]='Fizz'
    	for i in five : ans[i-1]='Buzz'
    	for i in fif : ans[i-1]="FizzBuzz"
    	return ans



if __name__ == "__main__":
	ans= Solution()
	print([i for i in ans.fizzBuzz(15)])