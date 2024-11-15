import turtle


# Create the UI for the game
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A maze game")
wn.setup(700, 700)


# Create Levels list
levels = [""]

# Define first level
level_1 = ["XXXXXXXXXXX",
           "XXXX   XXXX"]


# Create Pen
class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)    
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

pen = Wall()

# Create level setup function
def setup_maze(level):
    for 

# Create class instances
pen = Wall()

