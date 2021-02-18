from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color:
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What would you like to draw ('rectangle', 'square', or 'quit' to quit)? ")

    # If user enters rectangle
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter the rectangle's x coordinate: "))
        rec_y = int(input("Enter the rectangle's y coordinate: "))
        rec_width = int(input("Enter the rectangle's width: "))
        rec_height = int(input("Enter the rectangle's height: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))

        # Draw the rectangle
        rectangle = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        rectangle.draw(canvas)

    # If user enters rectangle
    if shape_type.lower() == "square":
        square_x = int(input("Enter the square's x coordinate: "))
        square_y = int(input("Enter the square's y coordinate: "))
        square_side = int(input("Enter the square's side: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green should the square have? "))
        blue = int(input("How much blue should the square have? "))

        # Draw the rectangle
        square = Square(x=square_x, y=square_y, side=square_side, color=(red, green, blue))
        square.draw(canvas)

    # Handle quit
    if shape_type == "quit":
        break

canvas.make('canvas2.png')
