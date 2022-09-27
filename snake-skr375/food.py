class Food:

	def __init__(self, ui, WIDTH, HEIGHT):
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		self.x = None
		self.y = None

	def generate_new_coordinates(self, ui, snake, wall_list):
		self.x = ui.random(self.WIDTH)
		self.y = ui.random(self.HEIGHT)
		for coordinate in snake.row:
			if (coordinate.x == self.x) and (coordinate.y == self.y):
				self.generate_new_coordinates(ui, snake, wall_list)
		for coordinate in wall_list.row:
			if (coordinate.x == self.x) and (coordinate.y == self.y):
				self.generate_new_coordinates(ui, snake, wall_list)

	def place(self, ui, snake, wall_list):
		self.generate_new_coordinates(ui, snake, wall_list)
		ui.place(self.x, self.y, ui.FOOD)
		ui.show()