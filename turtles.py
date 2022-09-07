# import turtle             # Allows us to use turtles
# wn = turtle.Screen()      # Creates a playground for turtles
# alex = turtle.Turtle()    # Create a turtle, assign to alex

# alex.forward(50)          # Tell alex to move forward by 50 units
# alex.left(90)             # Tell alex to turn by 90 degrees
# alex.forward(30)          # Complete the second side of a rectangle

# wn.mainloop()             # Wait for user to close window





# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")      # Set the window background color
# wn.title("Hello, Tess!")      # Set the window title

# tess = turtle.Turtle()
# tess.color("blue")            # Tell tess to change her color
# tess.pensize(3)               # Tell tess to set her pen width

# tess.forward(50)
# tess.left(120)
# tess.forward(50)

# wn.mainloop()




# import turtle
# wn = turtle.Screen()         # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# wn.title("Tess & Alex")

# tess = turtle.Turtle()       # Create tess and set some attributes
# tess.color("hotpink")
# tess.pensize(5)

# alex = turtle.Turtle()       # Create alex

# tess.forward(80)             # Make tess draw equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)               # Complete the triangle

# tess.right(180)              # Turn tess around
# tess.forward(80)             # Move her away from the origin

# alex.forward(50)             # Make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

# wn.mainloop()


import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                # This is new
size = 20
for i in range(30):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her

wn.mainloop()