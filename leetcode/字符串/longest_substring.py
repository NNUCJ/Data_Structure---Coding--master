'''
leetcode No.3 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
--直接使用暴力法，时间肯定超出限制。

'''
def function(s):
	if len(s) == 0:
		return 0
	elif len(s) == 1:
		return 1
	else:
		max_len = 0
		exit_s = []
		for i in s:
			if i not in exit_s:
				exit_s.append(i)
				max_len = max(max_len, len(exit_s))
			else:
				exit_s.pop

				exit_s.append(i)
				max_len = max(max_len, len(exit_s))
		return max_len


if __name__ == '__main__':
	s= "dvdf"
	result = function(s)
	print(result)
	