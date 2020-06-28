'''
leetcode No.746
使用最小花费爬楼梯, 解题的思路就是递归的思想，
最小的花费肯定包括本次的花费，
再选择前面的一步或者两步当中小的
f[i] = cost[i] + min(f[i+1], f[i+2])

'''
def solution(cost):

	f1 = f2 = 0
	for x in reversed(cost):
		f1, f2 = x + min(f1, f2), f1
	return min(f1, f2)






if __name__ == "__main__":
	cost = [10, 15, 20]
	out = solution(cost)
	print(out)
