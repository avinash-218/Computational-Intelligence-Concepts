class Points:
	def __init__(self, x, y, c):
		self.x = x #x coordinate
		self.y = y #y coordinate
		self.c = c #class id

	def calc_distance(self, x, y):
		#x,y - new point coordinates
		return (((self.x-x)**2 + (self.y-y)**2)**0.5, self.c)

def get_points(num_points, train_points):
	for i in range(num_points):
		print('Coordinates and Class of point {}(starting from zero): '.format(i+1), end='')
		x,y,c = map(int, input().split())
		train_points.append(Points(x,y,c))

def calc_distance_points(train_points):
	for point in train_points:
		dist_class.append(point.calc_distance(x,y))

def get_majority(k, dist_class, class_freq_count):
	print(dist_class)
	dist_class.sort()
	print('\n\n',dist_class)

	for i in range(k):
		class_freq_count[dist_class[i][1]]+=1

	return class_freq_count.index(max(class_freq_count))

if __name__ == '__main__':
	num_classes = int(input("Number of classes: "))
	num_points = int(input("Number of Points: "))
	train_points = []
	dist_class = []
	class_freq_count = [0]*num_classes

	get_points(num_points, train_points)

	x,y = map(int, input('Coordinates of unknown point :').split())
	k = int(input("Number of Neighbours to consider (odd number): "))

	calc_distance_points(train_points)
	
	print('\n\nClass:',get_majority(k, dist_class, class_freq_count))