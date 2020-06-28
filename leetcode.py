nums = [2,3,1,2,4,3]
n = 7

class Solution:
    def minSubArrayLen(self, s: int, nums):
        if not nums:
            return 0
        else:
            left = 0
            tmp_sum = 0
            res = float('inf')
            for right in range(len(nums)):
                tmp_sum += nums[right]
                while tmp_sum >= s:
                    res = min(res, right - left + 1)
                    tmp_sum -= nums[left]
                    left += 1
        return res if res != float('inf') else 0

fun = Solution()
res = fun.minSubArrayLen(n, nums)
print(res)
