front=[[1,1,1],[1,1,1],[1,1,1]]
right=[[2,2,2],[2,2,2],[2,2,2]]
back=[[3,3,3],[3,3,3],[3,3,3]]
left=[[4,4,4],[4,4,4],[4,4,4]]
top=[[5,5,5],[5,5,5],[5,5,5]]
bottom=[[6,6,6],[6,6,6],[6,6,6]]
cube={front: front, right: right, back: back, left: left, top: left, bottom: bottom}

print(cube)

class Cube:
	def __init__(self, cube):
		self.left = cube.left
		self.right = cube.right
		self.bottom = cube.bottom
		self.top = cube.top
		self.front = cube.front
		self.back = cube.back
	def R(self):
		copyFront = copy(self.front)

		# bottom goes to front
		self.front[0][2] = self.bottom[0][2]
		self.front[1][2] = self.bottom[1][2]
		self.front[2][2] = self.bottom[2][2]

		# back goes to bottom
		self.bottom[0][2] = self.back[0][2]
		self.bottom[1][2] = self.back[1][2]
		self.bottom[2][2] = self.back[2][2]

		# top goes to back
		self.back[0][2] = self.top[0][2]
		self.back[1][2] = self.top[1][2]
		self.back[2][2] = self.top[2][2]

		# front goes to top
		self.top[0][2] = copyFront[0][2]
		self.top[1][2] = copyFront[1][2]
		self.top[2][2] = copyFront[2][2]
