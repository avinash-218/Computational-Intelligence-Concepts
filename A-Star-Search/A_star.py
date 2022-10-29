def add_node(num_nodes, graph):
	graph[num_nodes] = dict()
	graph[num_nodes]['adj'] = []#adjacency list
	graph[num_nodes]['cost'] = []#cost list
	num_nodes+=1
	return num_nodes

def add_edge(u, v, graph, cost):
	graph[u]['adj'].append(v)
	graph[v]['adj'].append(u)

	graph[u]['cost'].append(cost)
	graph[v]['cost'].append(cost)

def display_graph(graph, h, num_nodes):
	print("\nNumber of nodes :", num_nodes)
	print("Heuristic Values:", h)
	print("Adjacency Lists :")
	print(graph)

def A_star_search(num_nodes, graph, h, start, end):
	path = [[start]]#add start node to path
	cost = [h[start]]#add start node's h value to cost
	min_cost = 999#to track min cost of path so far
	opti_path = None#to store opti path

	while(path):
		cur_path = path.pop(0)#get first path and its cost out of all
		cur_cost = cost.pop(0)

		if(cur_cost>min_cost):#if current cost is more than so far found min_cost, skip this path and its branches
			continue

		if(cur_path[-1] == end):#if end is reached
			if(cur_cost < min_cost):#if current cost is min than so far found min_cost
				opti_path = cur_path[:]#set the opti path as current path COPY
				min_cost = cur_cost#set min cost as current cost
			continue#go to next loop

		l = len(graph[cur_path[-1]]['adj'])#count number of adjacent nodes for the end node of current path
		for i in range(l):#loop through each adjacent nodes
			new_node = graph[cur_path[-1]]['adj'][i]#get ith adjacent node

			if(new_node in cur_path):#if it is already present in the path , skip it
				continue

			cur_path.append(new_node)#else add the adjacent node to the current path
			path.insert(0, cur_path[:])#insert the COPY of modified current path to the path list
			cur_path.pop()#pop the adjacent node inserted (to insert next adjacent node)
			c = cur_cost  - h[cur_path[-1]] + graph[cur_path[-1]]['cost'][i] + h[new_node]#calculate new path cost
			cost.insert(0, c)#insert the cost of modified new path

	return opti_path, min_cost #return optimal path and minimum cost

if __name__ == '__main__':
	num_nodes = 0
	graph = dict()
	h = []
	while(True):
		print("1. Add Node")
		print("2. Add Edge")
		print("3. A* Search")
		print("4. Display Graph")
		print("5. Exit")
		choice = input("Enter your choice:\n")

		if(choice=='1'):#add node
			h.append(int(input("Heuristic Value: ")))
			num_nodes = add_node(num_nodes, graph)
		
		elif(choice=='2'):#add edge
			edge = list(map(int, input("Enter edges as u v\n").split()))
			u, v = edge[0], edge[1]
			cost = int(input("Enter Cost of the Edge\n"))
			add_edge(u,v,graph, cost)
		
		elif(choice=='3'):#a star search
			start = int(input("Enter start node: "))
			end = int(input("Enter end node: "))
			opti_path, opti_cost = A_star_search(num_nodes, graph, h, start, end)

			print("\n\nOptimum Path:",opti_path)
			print("Optimum Cost:", opti_cost)
		
		elif(choice=='4'):#display graph
			display_graph(graph, h, num_nodes)
		
		elif(choice=='5'):
			break
		
		else:
			print("Invalid Option")

		print()