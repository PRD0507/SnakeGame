from turtle import Turtle
STARTING_POSITION = [(0,0), (-20, 0), (-40,0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        seg1 = Turtle()
        seg1.color("white")
        seg1.penup()
        seg1.shape("square")
        seg1.goto(position)
        self.segment.append(seg1)
    
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)

    def up(self):
       if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

