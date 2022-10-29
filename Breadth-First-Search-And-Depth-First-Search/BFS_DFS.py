def add_node(num_nodes, edges):
	edges[num_nodes] = []
	num_nodes+=1
	return num_nodes

def add_edge(u, v, edges):
	edges[u].append(v)
	edges[v].append(u)

def display_graph(edges,num_nodes):
	print("\nNumber of nodes :", num_nodes)
	print("Adjacency Lists :")
	print(edges)

def BFS(edges, start, end):#using queue
	visited = [False]*len(edges)
	queue = []
	output = []

	queue.append(start)
	visited[start] = True

	while(queue):
		ele = queue.pop(0)
		output.append(ele)
		if(ele == end):
			break

		for i in edges[ele]:
			if(visited[i]==False):
				visited[i] = True
				queue.append(i)
	return output

def DFS(edges, start, end):#using stack
	visited = [False]*len(edges)
	stack = []
	output = []

	stack.append(start)
	visited[start] = True

	while(stack):
		ele = stack.pop()
		output.append(ele)
		if(ele == end):
			break

		for i in edges[ele]:
			if(visited[i]==False):
				visited[i] = True
				stack.append(i)
	return output

if __name__ == '__main__':
	num_nodes = 0
	edges = dict()
	while(True):
		print("1. Add Node")
		print("2. Add Edge")
		print("3. DFS")
		print("4. BFS")
		print("5. Display Graph")
		print("6. Exit")
		choice = input("Enter your choice:\n")
		if(choice=='1'):#add node
			num_nodes = add_node(num_nodes, edges)
		elif(choice=='2'):
			edge = list(map(int, input("Enter edges as u,v\n").split()))
			u, v = edge[0], edge[1]
			add_edge(u,v,edges)
		elif(choice=='3'):
			start = int(input("Enter start node: "))
			end = int(input("Enter end node: "))
			output = DFS(edges, start, end)
			print("Traversal :", output)
		elif(choice=='4'):
			start = int(input("Enter start node: "))
			end = int(input("Enter end node: "))
			output = BFS(edges, start, end)
			print("Traversal :", output)
		elif(choice=='5'):
			display_graph(edges, num_nodes)
		elif(choice=='6'):
			break
		else:
			print("Invalid Option")

		print()