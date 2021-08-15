
##  Summary


### 二叉树的遍历

```

二叉树的前序遍历，中序遍历和后续遍历

递归法：

    前序遍历:
    
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)
    
    中序遍历：
    
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
    
    后续遍历：
    
            self.inorder(root.right, res)
            res.append(root.val)
            self.inorder(root.left, res)


        
迭代法(颜色标记): 利用栈先进后出的特性，模拟遍历过程中树的节点的访问过程，又因为栈先进后出的特性，入栈顺序为访问节点的顺序的逆序


    前序遍历:


        stack.append((WHITE, node.right))
        stack.append((WHITE, node.left))
        stack.append((GRAY, node)) 
        
    
    中序遍历:


        stack.append((WHITE, node.right))
        stack.append((GRAY, node))
        stack.append((WHITE, node.left))
        
    
    后续遍历:


        stack.append((WHITE, node.left))
        stack.append((GRAY, node))
        stack.append((WHITE, node.right))

 

```


### 二叉树的深度

```

递归法： DFS, 基于栈, 树的深度等于其左右子树的最大深度加1

        max(self.solution_1(root.left), self.solution_1(root.right)) + 1


迭代法:  BFS, 基于队列, 队列中存储当前层的所有节点，当当前层的所有节点出队后，则树的深度加1.



```
