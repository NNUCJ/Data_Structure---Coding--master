'''
	本题leetcode 第16题,思路：对list 先进行排序，后使用双指针
'''
def solution(nums, target):

	nums.sort()
	n = len(nums)
	temp_min = 0 # 用来存储目前的最小值

	for i in range(n):
		#设置双指针，缩小复杂度
		left = i+1
		rihgt = n-1
		while left < rihgt:
			sum_3 = nums[i] + nums[left] + nums[rihgt]
			diff = target - sum_3
			if temp_min == 0:
				temp_min =abs(diff)
				sum_min = sum_3

			if abs(diff) < temp_min:
				temp_min = abs(diff)
				sum_min = sum_3

			if sum_3 == target:
				return target
			elif sum_3 > target:
				rihgt -= 1
			elif sum_3 < target:
				left += 1
	return sum_min


