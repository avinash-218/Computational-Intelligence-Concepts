def add_node(graph, name):
	graph[name]=dict()
	graph[name]['adj']=[]
	graph[name]['visit']=False

def add_edge(graph, u, v):
	graph[u]['adj'].append(v)
	graph[v]['adj'].append(u)

def BFS(graph, start, end):
	bfs_path = []
	queue=[start]

	graph[start]['visit']=True

	while(queue):
		temp = queue.pop(0)#pop first element
		bfs_path.append(temp)#add the element to path

		if(temp==end):
			break

		for i in graph[temp]['adj']:
			if(graph[i]['visit']==False):
				graph[i]['visit']=True
				queue.append(i)

	return bfs_path

def DFS(graph, start, end):
	dfs_path = []
	stack=[start]

	graph[start]['visit']=True

	while(stack):
		temp = stack.pop()#pop first element
		dfs_path.append(temp)#add the element to path

		if(temp==end):
			break

		for i in graph[temp]['adj']:
			if(graph[i]['visit']==False):
				graph[i]['visit']=True
				stack.append(i)

	return dfs_path

if __name__=='__main__':
	graph = dict()
	while(True):
		print('1 - Add Node')
		print('2 - Add Edge')
		print('3 - Display Graph')
		print('4 - BFS')
		print('5 - DFS')
		print('6 - Exit')

		ch = int(input())
		print(ch)

		if(ch==1):
			name = input('Enter Node Name : ')
			print(name)
			add_node(graph, name)
		elif(ch==2):
			u, v = input('Enter edge as u v : ').split()
			print(u,v)
			add_edge(graph, u, v)
		elif(ch==3):
			print(graph)
		elif(ch==4):
			start, end = input('Enter starting and ending node : ').split()
			print(start, end)
			bfs_path = BFS(graph, start, end)
			print('BFS Path -', bfs_path)
		elif(ch==5):
			start, end = input('Enter starting and ending node : ').split()
			print(start, end)
			dfs_path = DFS(graph, start, end)
			print('DFS Path -', dfs_path)
		elif(ch==6):
			break
		else:
			print('Invalid Input')