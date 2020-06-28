'''
leetcode No.198
solution1 采用的是递归的方式，从数组的最后两位开始，如果选择最后一个，则在nums[:n - 2]寻找最大的
												 如果选择倒数第二个，则在num[:n-3]中寻找一个最大的
但是soulution的方法超出额时间限制

solution2 动态规划的方式
'''



def solution1(nums):
	max_mony = 0
	n = len(nums)
	if n == 0:
		return max_mony
	if n == 1:
		max_mony += nums[0]
		return max_mony
	if n == 2:
		max_mony += max(nums)
		return max_mony
	if n == 3:
		max_mony += max(nums[0]+nums[2], nums[1])
		return max_mony
	if n > 3:
		#while i>=4
		max_mony = max(nums[n-1] + solution(nums[:n - 2]), nums[n - 2] + solution(nums[:n - 3]))
			
		return max_mony

def solution2(nums):
	'''
	'''
	premax = 0
	currmax = 0
	for i in nums:
		temp = currmax
		currmax = max(i + premax, currmax)
		premax = temp
	return currmax

if __name__ == "__main__":

	#nums = [1,2,3,1]
	nums = [2,7,9,3,1]
	mony = solution2(nums)
	print(mony)
