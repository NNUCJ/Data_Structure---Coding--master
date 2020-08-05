# 打家劫舍 iii

[leetcode 337](https://leetcode-cn.com/problems/house-robber-iii/)，从题目描述中可以看出，`[3,2,3,null,3,null,1]`构建的二叉树中左右子树只有一支，并且由于不能在直接相连的两个结点上进行打劫，`i`结点后的`i+2`结点中找一个最大元素。



## 1.题解
&emsp;&emsp;可以采用动态规划的方式进行求解，动态规划的一般步骤如下：
* 定义状态（最优子结构、大量重复子问题）
* 寻找决策（状态转移方程）
* 确定初值（边界条件）

1. 定义状态
&emsp;&emsp;对上述的问题树的每个结点都有两个状态，被选中以及没有被选中两个状态。使用`f(0)`表示o结点被选中的最大的收益，`g(o)`表示o结点不被选中的情况下，字数上的被选择的最大收益。  

2.状态转移方程

&emsp;&emsp;当o被选中的时候，o的左右孩子不能被选中，此时最大收益为结点o的收益加上。左右孩子不被选中情况下的最大收益，即：`f(o)=g(l)+g(r)`;(l, r表示o结点的左右孩子)  
&emsp;&emsp;当 oo 不被选中时，oo 的左右孩子可以被选中，也可以不被选中。对于 oo 的某个具体的孩子 xx，它对 oo 的贡献是 xx 被选中和不被选中情况下权值和的较大值。故 `g(o) = max{f(l) , g(l)}+max{f(r), g(r)}`




    class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            [l_rob, l_not_rob] = dfs(node.left)
            [r_rob, r_not_rob] = dfs(node.right)
            return [node.val + l_not_rob + r_not_rob, max([l_rob, l_not_rob]) +  max([r_rob, r_not_rob])]
        return max(dfs(root))

