from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_blocks(positions)

    def add_blocks(self, positions):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(positions)
        self.blocks.append(t)

    def extend(self):
        self.add_blocks(self.blocks[-1].position())

    def move(self):
        for block_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
