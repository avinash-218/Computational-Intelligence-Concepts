def add_node(graph, name):
	graph[name]=dict()
	graph[name]['adj']=[]
	graph[name]['cost']=[]
	graph[name]['visit']=False

def add_edge(graph, u, v, cost):
	graph[u]['adj'].append(v)
	graph[u]['cost'].append(cost)

	graph[v]['adj'].append(u)
	graph[v]['cost'].append(cost)

def UCS(graph, start, end):
	priority_queue = [(start,0)]#start node with distance

	while(priority_queue):
		temp = priority_queue.pop(0)#pop starting element (node, cost)
		last_node = temp[0][-1]#last node reached
		graph[last_node]['visit']=True#set as visited

		if(last_node==end):#if last node is end, return cost after inserting the last node
			priority_queue.insert(0, temp)
			break

		last_cost = temp[1]#so far cost

		for next_node in graph[last_node]['adj']:#all adjacent nodes of last node
			if(graph[next_node]['visit']==False):#if unvisited
				ind = graph[last_node]['adj'].index(next_node)#get the index of adjacent nodes, to access corresponding cost
				iter_nodes = (temp[0]+next_node, last_cost+graph[last_node]['cost'][ind])#find path and calc cost of adjacents
				priority_queue.append(iter_nodes)#append the path and its cost
		
		priority_queue.sort(key = lambda x : x[1])#sort priority key by cost

	return priority_queue[0]#return first element (min cost path, min cost)

if __name__=='__main__':
	graph = dict()
	while(True):
		print('1 - Add Node')
		print('2 - Add Edge')
		print('3 - Display Graph')
		print('4 - UCS')
		print('5 - Exit')

		ch = int(input())
		print(ch)

		if(ch==1):
			name = input('Enter Node Name : ')
			print(name)
			add_node(graph, name)
		elif(ch==2):
			u, v, cost = input('Enter edge as u v and cost: ').split()
			cost=int(cost)
			print(u,v, cost)
			add_edge(graph, u, v, cost)
		elif(ch==3):
			print(graph)
		elif(ch==4):
			start, end = input('Enter starting and ending node : ').split()
			print(start, end)
			ucs_path = UCS(graph, start, end)
			print('UCS Path -', ucs_path)
		elif(ch==5):
			break
		else:
			print('Invalid Input')