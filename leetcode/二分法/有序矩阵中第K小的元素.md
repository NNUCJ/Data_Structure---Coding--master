# 有序矩阵中第K小的元素
[题目leetcode378](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)
## 1.题解
&emsp;&emsp;题目中需要的注意的是排序的好的矩阵只满足每行每列升序，不代表`A[0][n]`>`A[1][0]`

    matrix = [              
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
    ],

### 1.1 直接法
&emsp;&emsp;最直接的方法就是将矩阵转换成list，然后对list重新进行排序，时间复杂度
主要取决于与n*n个元素进行排序，代码如下：

    from typing import List
    class Solution:
        def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
            res = sorted(sum(matrix, []))  # 
            return res[k - 1]
    
    
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    
    S = Solution()
    res = S.kthSmallest(matrix, k=8)
    print(res)
&emsp;&emsp;对于直接法没有考虑到二维数组的特点，暴力求解。该题根据每行的特性利用归并排序
[参考链接](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/shi-yong-dui-heapde-si-lu-xiang-jie-ling-fu-python/)

### 1.2 二分法
&emsp;&emsp; 此处采用的二分法与在一维数组中采用二分法存在一些略微的区别，但是二分法基本模板还是如下：

            while left < right:
                mid = (left + right)
                if（更新条件）:  
                   right = mid 
                else:
                    left  = mid + 1
            return left

&emsp;&emsp; 在矩阵中，`A[0][0]`是最小值，`A[n-1][n-1]`是最大值，以左下角的元素为起点

&emsp;&emsp;统计的步骤：

1. 如同当前的元素小于或等于mid,则计算加一，并且往右继续比较；
2. 当前元素大于mid时，则向上移动

&emsp;&emsp;由于小于mid的值都会在 [分割线](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/)
的左上部分，左右两端的更新条件，

1. 计数的数目不小于K, 则说明最终的输出结果小于mid
2. 计数的数目小于K，则说明最终的输出结果大于mid

（简单点理解就是如果mid是程序找到第K个小的数，但是计数的过程中小于等于mid的数多余K个，是不是就前后矛盾了）

代码：

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
        left, right = matrix[0][0], matrix[-1][-1]
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