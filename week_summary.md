

## DFS

```

def dfs(node, visited):

   # 判断node是否已经被访问
   if node in visited：
       return
       
   
   # 处理当前层
   visited.add(node)
   
   
   # dill down
   dfs(next_node, visited)

    

```


## BFS 

```

def nfs(node, queue):

   queue = []
   
   while queue:
   
       node = queue.popleft()
       
       process(node)
       
  
       nodes = get_related_nodes(node)
       if nodes:
           queue.push(nodes)
       



```