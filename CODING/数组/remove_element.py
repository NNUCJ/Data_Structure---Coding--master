'''
leetcode No.27,使用双指针

'''
def function(nums, vol):
	i = 0
	n =len(nums)
	for j in range(0, n):
		if nums[j] != vol:
			nums[i] = nums[j]
			i += 1
	return i





if __name__  == '__main__':
	nums = [3, 2, 2, 3]
	i = function(nums, 3)
	print(i)
	