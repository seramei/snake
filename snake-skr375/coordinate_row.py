class CoordinateRow:
	
	def __init__(self):
		self.row = []

	def add(self, Coordinate):
		self.row.append(Coordinate)

	def get_head_x(self):
		return self.row[-1].x

	def get_head_y(self):
		return self.row[-1].y

	def detect_collision(self, object):
		return (self.get_head_x() == object.x) and (self.get_head_y() == object.y)

	def delete_tail(self): # deletes the last position of the snake each time the snake moves
		del self.row[0]
