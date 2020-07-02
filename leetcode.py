
#
# nums = [2,3,1,2,4,3]
# n = 7
#
# class Solution:
#     def minSubArrayLen(self, s: int, nums):
#         if not nums:
#             return 0
#         else:
#             left = 0
#             tmp_sum = 0
#             res = float('inf')
#             for right in range(len(nums)):
#                 tmp_sum += nums[right]
#                 while tmp_sum >= s:
#                     res = min(res, right - left + 1)
#                     tmp_sum -= nums[left]
#                     left += 1
#         return res if res != float('inf') else 0
#
# fun = Solution()
# res = fun.minSubArrayLen(n, nums)
# print(res)

# leetcode378
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k):
        n = len(matrix)
        def check_mid(mid):
            i, j = n-1, 0  # i 表示行，j表示列
            cnt = 0
            while i >=0 and j <= n-1:
                if matrix[i][j] <= mid:
                    cnt += i + 1   # 加i的原因是最后一列的数肯定是最大的，因此小于mid的个数可以直接加行数
                    j += 1
                else:
                    i -= 1
            return cnt >= k

        # 确定二分法的两个区间
        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = (left + right) // 2
            if check_mid(mid):
               right = mid
            else:
                left = mid + 1
        return left


matrix = [
             [1, 5, 9],
             [10, 11, 13],
             [12, 13, 15]
         ]

S = Solution()
res = S.kthSmallest(matrix, k=8)
print(res)