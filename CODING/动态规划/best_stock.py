'''
leetcode No.121

'''
def solution(prices):
	"""
	暴力法，但是这样的解法再leetcode中超出时间限制
	用listq去记录最大profit
	"""

	n = len(prices)
	if n < 2:
		return 0
	elif n == 2:
		if prices[1] - prices[0] <= 0:
			return 0
		else:
			return 1
	else:
		max_profit = []
		index = []
		for i in range(len(prices)-1):
			temp_array = prices[i+1:]
			max_temp= max(temp_array)
			profit = max_temp-prices[i]
			max_profit.append(profit)
			index.append(prices.index(max(prices[i+1:])))
		if max(max_profit) <= 0 :
			return 0
		else:
			return  max(max_profit)


def solution2(prices):
	'''
	记录【今天之前买入的最小值】
	计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
	比较【每天的最大获利】，取最大值即可
	'''
	n = len(prices)
	if n < 2:
		return 0
	else:
		min_price = prices[0]
		max_profit = 0
		for i in range(1, n):
			max_profit = max(max_profit, prices[i]-min_price)
			min_price = min(prices[i], min_price)
		return max_profit 

if __name__ == '__main__':
	prices = [2,1,4]

	max_profit = solution2(prices)
	print(max_profit)