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

def display_graph(graph, num_nodes):
	print("\nNumber of nodes :", num_nodes)
	print("Adjacency Lists :")
	print(graph)

def uniform_cost_search(num_nodes, graph, start, end):
	nodes = list(range(num_nodes))
	adj_nodes =[[0, start]]#open list to keep track of adjacent nodes with cost
	selected_nodes = []#closed list to keep track of selected nodes with cost
	visited = len (nodes)*[False]#visited list to avoid duplication of nodes in adj_nodes
	visited [start] = True
	path = []

	while(adj_nodes):
		current_node = min(adj_nodes)#adjacent node with min weight
		pop_index = adj_nodes.index(current_node)#index of considered node

		adj_nodes.pop(pop_index)#remove the considered node
		selected_nodes.append(current_node)#considered node added
		path.append(current_node)#add considered node to path

		if(current_node[1]==end):#if reached end node
			break
		
		for node in adj_nodes:#update the weight of existing nodes according to currently chosen node
			if(node[1] in graph[current_node[1]]["adj"]):
				#calculate new distance of the nodes adjacent to current node.
				new_dist = current_node[0] + graph[node[1]]["cost"][graph[node[1]]["adj"].index(current_node[1])]
				
				if(node[0]>new_dist):#update the distance of node if new_distance is lesser than old.
					node[0] = new_dist
					
		adj_list=graph[current_node[1]]["adj"]
		cost = graph[current_node[1]]["cost"]
		
		for node in adj_list:#add adjacent nodes of current_node in adj_nodes
			if (not visited[node]):
				visited [node] = True
				adj_nodes.append([current_node[0] + cost[adj_list.index(node)], node])

	return path , selected_nodes[-1][0]	

if __name__ == '__main__':
	num_nodes = 0
	graph = dict()
	while(True):
		print("1. Add Node")
		print("2. Add Edge")
		print("3. Uniform Cost Search")
		print("4. Display Graph")
		print("5. Exit")
		choice = input("Enter your choice:\n")
		if(choice=='1'):#add node
			num_nodes = add_node(num_nodes, graph)
		elif(choice=='2'):
			edge = list(map(int, input("Enter edges as u v\n").split()))
			u, v = edge[0], edge[1]
			cost = int(input("Enter Cost of the Edge\n"))
			add_edge(u,v,graph, cost)
		elif(choice=='3'):
			start = int(input("Enter start node: "))
			end = int(input("Enter end node: "))
			path , optimal_cost = uniform_cost_search(num_nodes, graph, start, end)
			print ( "\nPath:" )
			for node in path:
				print( node [ 1 ] , end = " " )
			print( "\nCost: " , optimal_cost )
		elif(choice=='4'):
			display_graph(graph, num_nodes)
		elif(choice=='5'):
			break
		else:
			print("Invalid Option")

		print()