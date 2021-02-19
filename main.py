from get_sanitized_input import *
from canvas import Canvas
from shapes import Rectangle, Square

MAX_CANVAS_SIZE = 2000

# Get canvas width and height from user
canvas_width = get_sanitized_input("Enter canvas width: ", int, 0, MAX_CANVAS_SIZE)
canvas_height = get_sanitized_input("Enter canvas height: ", int, 0, MAX_CANVAS_SIZE)


# Make a dictionary of color codes and prompt for color:
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = get_sanitized_input(
    "Enter canvas color (white, black, or 'quit' to quit): ",
    str.lower, range_=('white', 'black', 'quit'))
if canvas_color == "quit":
    quit()

# Create a canvas with user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = get_sanitized_input(
        "What would you like to draw (rectangle, square, or 'quit' to quit): ",
        str.lower, range_=('rectangle', 'square', 'quit')
    )

    # If user enters rectangle
    if shape_type.lower() == "rectangle":
        rec_width = get_sanitized_input("Enter the rectangle's width: ", int, 1, canvas_width)
        rec_height = get_sanitized_input("Enter the rectangle's height: ", int, 1, canvas_height)
        rec_x = get_sanitized_input("Enter the rectangle's x coordinate: ", int, 0, canvas_width - rec_width)
        rec_y = get_sanitized_input("Enter the rectangle's y coordinate: ", int, 0, canvas_height - rec_height)

        red = get_sanitized_input("How much red should the rectangle have? ", int, 0, 255)
        green = get_sanitized_input("How much green should the rectangle have? ", int, 0, 255)
        blue = get_sanitized_input("How much blue should the rectangle have? ", int, 0, 255)

        # Draw the rectangle
        rectangle = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        rectangle.draw(canvas)

    # If user enters rectangle
    if shape_type.lower() == "square":
        square_side = get_sanitized_input(
            "Enter the square's side: ", int, 1,
            canvas_width if canvas_width < canvas_height else canvas_height)
        square_x = get_sanitized_input("Enter the square's x coordinate: ", int, 0, canvas_width - square_side)
        square_y = get_sanitized_input("Enter the square's y coordinate: ", int, 0, canvas_height - square_side)
        red = get_sanitized_input("How much red should the square have? ", int, 0, 255)
        green = get_sanitized_input("How much green should the square have? ", int, 0, 255)
        blue = get_sanitized_input("How much blue should the square have? ", int, 0, 255)

        # Draw the square
        square = Square(x=square_x, y=square_y, side=square_side, color=(red, green, blue))
        square.draw(canvas)

    # Handle quit
    if shape_type == "quit":
        break

canvas.make('canvas.png')
