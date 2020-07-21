# 构建二叉树

## 0. 前言
&emsp;&emsp;在leetcode官网的编辑器中自动会生成测试用例， [如题](https://leetcode-cn.com/problems/path-sum/)
输入数据为List,如果本地的IDE中肯定无法直接使用List作为输入数据，这也是很多公司在做笔试编程时碰到的第一个问题，对输入
数据的构建。  
&emsp;&emsp;在leetcode中提供了如下的code定了tree类，但是此代码只是完成了对树的定义，没有能够从List完成对而树的构建。
本文对此进行解释说明。

    # Definition for a binary tree node.
     class TreeNode:
        def __init__(self, x):
           self.val = x
           self.left = None
           self.right = None

## 1. 构建二叉树
&emsp;&emsp;以此`[5,4,8,11,null,13,4,7,2,null,null,null,1]`作为测试用例来构建二叉树，由于二叉树的特殊性，更加容易实现。
`List[0]`肯定是作为树的根节点，后面的元素两两组队最为前一个的左右子树，进一步理解列表第1、第2个元素是作为第0个元素的左右子树，第3、第4个元素
是作为第1个元素的左右子树，因此list中当前位置处元素左右子树分别位于`2*index+1、 2*index+2`处。

&emsp;&emsp;代码如下：

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


    def create_Bitree(data, index):
        Pnode = None
        if index < len(data):
            if data[index]  is  None:
                return Pnode
            Pnode = TreeNode(data[index])
            Pnode.left = create_Bitree(data, 2*index + 1)
            Pnode.right = create_Bitree(data, 2 * index + 2)

         return Pnode

    data = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    for i in range(len(data)):
        Pnode = create_Bitree(data, 0)
    print(Pnode.left.val)
    
    >>> 4 ## 根节点的左子树的值

