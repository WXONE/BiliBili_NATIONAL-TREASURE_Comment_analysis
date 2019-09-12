# 二叉树中所有距离为K的结点

首先观察下二叉树是怎么构建的：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
```

啊，原来是基于父节点

那我们可以知道一个节点左右儿子的信息，但是无法知道其父节点的信息，这样我们先深度优先遍历，获取父节点信息，存在数组中，再进行一次深度优先遍历，查找所有距离为K的节点信息。

为了避免重复搜索用f数组进行标记

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ans = []
        def solve(root):
            if root==None:
                return -1
            if root == target:
                add_node(root,K)
                return 1
            L,R = solve(root.left), solve(root.right)
            if L!=-1:
                if L==K:
                    ans.append(root.val)
                else:
                    add_node(root.right, K-L-1)
                return L+1
            if R!=-1:
                if R==K:
                    ans.append(root.val)
                else:
                    add_node(root.left,K-R-1)
                return R+1
            return -1
        def add_node(root,L):
            if root==None:
                return
            if L==0:
                ans.append(root.val)
            else:
                add_node(root.left,L-1)
                add_node(root.right,L-1)
        solve(root)
        return ans

```

