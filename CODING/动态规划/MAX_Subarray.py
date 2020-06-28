'''
最大子数组和，leetcode No.53 
If you have figured out the O(n) solution, try coding another solution using 
the divide and conquer approach, which is more subtle.

'''
def solution(nums):
	'''
	动态规划实现O(N)
	'''
	max_sum = nums[0]
	temp_sum = 0
	for i  in nums:
		if temp_sum < 0:
			temp_sum = i
		else:
			temp_sum += i

		if temp_sum > max_sum:
			max_sum = temp_sum
	return max_sum


if __name__ == "__main__":
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	max_sum = solution(nums)
	print(max_sum)

