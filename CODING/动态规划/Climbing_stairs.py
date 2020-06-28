'''
leetcode No.70
到第i个台阶的办法，因为每次只能爬1层或者2层，只有两种从第i-1层或者第i-2层过来，
因此到第i层的办法就是，i-1与i-2的方法之和

dp[i] = dp[i-1] + dp[i-2]
'''

def solution(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n>=3:
		dp = [0 for i in range(n+1)]
		dp[1] = 1
		dp[2] = 2 
		for i in range(3, n+1):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[i]



if __name__ == "__main__":
	# dp = [0 for i in range(4)]
	print(solution(4))