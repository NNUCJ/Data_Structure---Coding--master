
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
# from typing import List
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k):
#         n = len(matrix)
#         def check_mid(mid):
#             i, j = n-1, 0  # i 表示行，j表示列
#             cnt = 0
#             while i >=0 and j <= n-1:
#                 if matrix[i][j] <= mid:
#                     cnt += i + 1   # 加i的原因是最后一列的数肯定是最大的，因此小于mid的个数可以直接加行数
#                     j += 1
#                 else:
#                     i -= 1
#             return cnt >= k
#
#         # 确定二分法的两个区间
#         left, right = matrix[0][0], matrix[n-1][n-1]
#         while left < right:
#             mid = (left + right) // 2
#             if check_mid(mid):
#                right = mid
#             else:
#                 left = mid + 1
#         return left
#
#
# matrix = [
#              [1, 5, 9],
#              [10, 11, 13],
#              [12, 13, 15]
#          ]
#
# S = Solution()
# res = S.kthSmallest(matrix, k=8)
# print(res)
from typing import List
import collections
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# def create_Bitree(data, index):
#     Pnode = None
#     if index < len(data):
#         if data[index]  is  None:
#             return Pnode
#         Pnode = TreeNode(data[index])
#         Pnode.left = create_Bitree(data, 2*index + 1)
#         Pnode.right = create_Bitree(data, 2 * index + 2)
#
#     return Pnode

# data = [5,4,8,11,None,13,4,7,2,None,None,None,1]
# for i in range(len(data)):
#     Pnode = create_Bitree(data, 0)
# print(Pnode.left.val)


# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:  # 可能存在树为空的情况
#             return False
#         que_node = collections.deque([root])   # 记录遍历的节点
#         que_val = collections.deque([root.val])  # 记录遍历节点的value
#         while que_node:
#             now = que_node.popleft()
#             temp_val = que_val.popleft()
#             if not now.left and not now.right:   # 处于叶子节点位置判断与目标值的关系
#                 if temp_val == sum:
#                     return True
#                 continue
#
#             if now.left:
#                 que_node.append(now.left)
#                 que_val.append(now.left.val + temp_val)
#
#             if now.right:
#                 que_node.append(now.right)
#                 que_val.append(now.right.val + temp_val)
#         return False
#
# data = [5,4,8,11,None,13,4,7,2,None,None,None,1]
#
# Pnode = create_Bitree(data, 0)
# # print(Pnode.left.left.val)
# sum = 22
# S = Solution()
# out = S.hasPathSum(Pnode, sum)
# print(out)

### leetcode 面试题16.11
# class Solution:
#     def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
#         res = []
#         if k == 0:
#             res.append(0)
#         else:
#             for i in range(k+1):
#                 tmp = i*shorter + (k-i)*longer
#                 res.append(tmp)
#         res_ = sorted(res)
#         return res_
#
# S =Solution()
# res = S.divingBoard(1, 1, 0)
# print(res)