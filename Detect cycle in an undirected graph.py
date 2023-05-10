from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
	    colors = [0 for _ in range(V)]
	    
		def dfs(node, parent):
		    if colors[node] == 1:
		        return True
		    colors[node] = 1
		    for child in adj[node]:
		       if child == parent:
		           continue
		       flag = dfs(child, node)
		       if flag:
		           return True
		       
		    colors[node] = 2
		    return False
		flag = False
		for i in range(V):
		    if colors[i] == 0:
		        flag = dfs(i, -1)
		        if flag:
		            return 1
		 
		return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
