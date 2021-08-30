

### 深度优先搜索和广度优先搜索

```

深度优先搜索：满足条件则drill down, 不满足则回退

递归写法:


visited = set()

def dfs(node, visited):

    if node in visited: # terminator
        # already visited 
        return
        
    for next_node in node.children(): 
        if next_node not in visited: 
            dfs(next_node, visited)
            
            
非递归写法:


def DFS(self, tree): 

    if tree.root is None: 
        return [] 
        
        
    while stack: 
    
        node = stack.pop() 
        visited.add(node)
        
        process (node) 
        nodes = generate_related_nodes(node) 
        stack.push(nodes) 
        
        # other processing work 


广度优先遍历: 遍历完当前层在去下一层

广度优先需要借助队里先出的特性

def BFS():
       
    visited = set()
    queue = [] 
    queue.append([start]) 
    
    while queue: 
    
        node = queue.pop() 
        visited.add(node)
        
        process(node) 
        nodes = generate_related_nodes(node) 
        queue.push(nodes)
        
    ... other works
    

对于深度优先遍历和广度优先遍历的重点要先抽象出搜索模型，
然后再决定用深度优先遍历还是广度优先遍历

```



### 贪心

```

贪心本质上指一种特殊的动态规划

贪心的前提条件是能通过局部最优解得到全局最优解

```


### 二分查找

```

二分查找的条件:


1） 单调性--有序性

2)  存在边界

3） 可以通过索引下标访问

```