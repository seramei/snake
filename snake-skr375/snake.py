''' Assignment: snake.py
	Created on 08-12-2019
	@author: Sarah Kwakkelaar '''


from ipy_lib import SnakeUserInterface
from coordinate import Coordinate
from coordinate_row import CoordinateRow
from food import Food


WIDTH = 32
HEIGHT = 24
SCALE = 1
ANIMATION_SPEED = 10 # frames per second


def move():
	x = snake.get_head_x()
	y = snake.get_head_y()
	if orientation == "r":
		snake.add(Coordinate(0,y)) if (x == WIDTH-1) else snake.add(Coordinate(x+1,y))
	elif orientation == "l":
		snake.add(Coordinate(WIDTH-1,y)) if (x == 0) else snake.add(Coordinate(x-1,y))
	elif orientation == "u":
		snake.add(Coordinate(x, HEIGHT-1)) if (y == 0) else snake.add(Coordinate(x,y-1))
	elif orientation == "d":
		snake.add(Coordinate(x,0)) if (y == HEIGHT-1) else snake.add(Coordinate(x,y+1))


def check_for_food():
	food.place(ui,snake, wall_coordinates_list) if snake.detect_collision(food) else snake.delete_tail()


# when the game ends (for any reason) the ui will simply close and the console will print "Game over!"
def endgame():
	print ("Game over!")
	ui.close()


def check_for_endgame():
	for coordinate in snake.row[:-1]:
		if snake.detect_collision(coordinate):
			endgame()
	for coordinate in wall_coordinates_list.row:
		if snake.detect_collision(coordinate):
			endgame()


def process_alarm(event):
	ui.place(snake.row[0].x, snake.row[0].y, ui.EMPTY)
	move()
	ui.place(snake.row[-1].x, snake.row[-1].y, ui.SNAKE)
	check_for_food()
	check_for_endgame()
	ui.show()


def process_arrow(event):
	global orientation
	if orientation == "r":
		if event.data != "l":
			orientation = event.data
	if orientation == "l":
		if event.data != "r":
			orientation = event.data
	if orientation == "u":
		if event.data != "d":
			orientation = event.data
	if orientation == "d":
		if event.data != "u":
			orientation = event.data


def process_event(event):
	if event.name == "arrow":
		process_arrow(event)
	if event.name == "alarm":
		process_alarm(event)


def initialize_ui():
	ui.set_animation_speed(ANIMATION_SPEED)
	for coordinate in start_coordinates:
		x_and_y = coordinate.split()
		snake.add(Coordinate(int(x_and_y[0]), int(x_and_y[-1])))
	for coordinate in wall_coordinates:
		if coordinate != "":
			x_and_y = coordinate.split()
			x = int(x_and_y[0])
			y = int(x_and_y[-1])
			wall_coordinates_list.add(Coordinate(x,y))
			ui.place(x,y, ui.WALL)
	food.place(ui,snake, wall_coordinates_list)


level = raw_input("Enter 1, 2, 3, or 4 to select a level.")
if level == "1":
	input_file = open("SnakeInput1.txt")
if level == "2":
	input_file = open("SnakeInput2.txt")
if level == "3":
	input_file = open("SnakeInput3.txt")
if level == "4":
	input_file = open("SnakeInput4.txt")

input_lines = input_file.read().split("=")
input_file.close()
start_coordinates = input_lines[0].split("\n")
orientation = input_lines[1].lower()
wall_coordinates = input_lines[-1].split("\n")
wall_coordinates_list = CoordinateRow()


snake = CoordinateRow()
ui = SnakeUserInterface(WIDTH, HEIGHT, SCALE)
food = Food(ui, WIDTH, HEIGHT)
initialize_ui()


while True:
	event = ui.get_event()
	process_event(event)


ui.stay_open()

