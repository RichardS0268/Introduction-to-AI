# using recursion
# for example, we want to search for a path of 4 in a graph
class Node(object):
	def __init__(self, val, nextNodes):
        self.val = val
        self.nextNodes = nextNodes
        
visited = []

def dfs(nodes, depth):
    if depth == 4: # satisfy the target
        return True
    for n in nodes.nextNodes:
        if n not in visited:
            visited.append(n)
            if dfs(n, depth+1): # using recursion to pass the signal of success upper 
                return True
        # reset unvisited, cause it may appare in another path    
        visited.remove(n)
    # there is no solution
    return Flase