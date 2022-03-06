# A-star Search

`A*` search is a popular and basic algorithm in searching problems. It is based on the BFS (Breadth First Search)

## Overview of several classical search algorithms

### 1. Breadth First Search (BFS)

#### **1.1 **Key Point

+ for a focus (i.e. the node on hand), we try to traverse the nodes around it. In order not to repeat the visit, we set a signal variable.
+ We prefer to choose the least deep node for search next

```python
frontier = Queue() # store nodes in Queue
frontier.put(start)
visited = {}
vistied[start] = True # having visited or not

while not frontier.empty():
    current = frontier.get()
    for next in graph.neighbors(current): # visti neighbors
        if next not in visited:
            frontier.put(next)
            visited[next] = True
```

#### 1.2 Search for shortest path

Since BFS always searches around a focus, it can find the shortest path as long as it finds a path. 

If we want to find the shortest path, we can record the source of next to go back. Besides, we can set a signal which shut down search as long as we find a path.

```python
frontier = Queue()
frontier.put(start)
came_from = {}
came_fron[start] = None 

while not frontier.empty():
    current = frontier.get()
    
    if current == goal: # if we find the path, break
        break
        
    for next in graph.neighbors(current):
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current
            
# go bach to formulate the path
current = goal
path = []
while current != start:
    path.append(current)
    current = came_from[current]
path.append(start) # optional
path.reverse() # optional ](https://leetcode.com/problems/perfect-squares/)
```

#### 1.3 Shortcomings

+ relatively blind search. When we want to find a way to the target, it may just start search from the other opposite direction.
+ Computation cost is high

### 2. Depth First Search (DFS)

#### 2.1 Key point

+ We prefer choose the deepest node for search next

+ DFS can be realized by recursion or stack

##### 2.1.1 A recursive implementation of DFS

```pseudocode
procedure DFS(G, v) is
	label v as discovered
	for all directed edges from v to w that are in G.adjacentEdges(v) do
		if vertex w is not labeled as discovered then
			recursively call DFS(G, w)
```

##### 2.1.2 Non-recursive implementation of DFS

The non-recursive implementation is similar to breadth-first search but differ from it in two ways:

+ it uses a  stack instead of a queue
+ it delays checking whether a vertex has been discovered until the vertex is popped from the stack rather than making this check before adding the vertex

A non-recursive implementation of DFS with worst-case space complexity ![O(|E|)](https://wikimedia.org/api/rest_v1/media/math/render/svg/976fe7f1e011d0dcdb3d6163754c877aaad5187f), with the possibility of duplicate vertices on the stack

```pseudocode
Procedure DFS_iterative1(G, v) is
	let S be a stack
	S.push(v)
	while S is not empty do
		v = S.pop()
		if v is not labeled as discovered then
			label v as discovered
			for all edges from v to w in G.adjacentEdges(v) do
				S.push(w)
```

Another possible implementation of iterative depth-first search uses a stack of iterators of the list of neighbors of a node, instead of a stack of nodes. This *yields the same traversal* as recursive DFS.

```pseudocode
procedure DFS_iterative(G, v) is
	let S be a stack
	S.push(iterator of G.adjacentEdges(v))
	while S is not empty do
		if S.peek().hasNext() then
			w = S.peek().next()
			if w is not labeled as discovered then
				label w as discovered
				S.push(iterator of G.adjacentEdges(w))
        else
        	S.pop()
```

### 3. Dijkstra's Algorithm

## A-star Search

