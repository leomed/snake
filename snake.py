from turtle import Turtle,Screen
#Constants in python are written in capital letters
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        """It initialize the object with its attributes, and
        methods
        """
        self.segments = []
        #This method is automatically called to create the snake
        #There other methods that maybe i do not want to be automatic
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        """It creates a new peace of the snake , and then
        its given a position so the parts of the same snake
        are place one next to each other
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        """
        It loops throw all the segments but in reverse, the idea is that
        the last peace moves to the second place, and the one that it is in the
        second to the first, as if the squares were following each other path
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        The snake cant move backwards in any direction,
        so this logics prevents that from happening

        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
