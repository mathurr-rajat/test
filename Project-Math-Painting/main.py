from canvas import Canvas
from shapes import Square,Rectangle

# get canvas width and height from the user
canvas_width = int(input("enter canvas width    "))
canvas_height = int(input("\nenter canvas height  "))

# make a dictionary of color and prompt for color
colors = {"white": (255,255,255), "black": (0,0,0)}
canvas_color = input("\nEnter canvas color (white or black):  ")

# create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


while True:
    user_input= input("\nwhat you would like to draw rectangle or square or quit    ")
    if user_input.lower() == 'rectangle':
        rec_x = int(input("\n enter x coordinate of rectangle    "))
        rec_y = int(input("\n enter y coordinate of rectangle  "))
        rec_width = int(input("\n enter width of rectangle  "))
        rec_height = int(input("\n enter height of rectangle  "))

        red = int(input("\nHow much red color you want, enter values between 0-255    "))
        green = int(input("\nHow much green color you want, enter values between 0-255    "))
        blue = int(input("\nHow much blue color you want, enter values between 0-255    "))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        # r1 = Rectangle(x=1, y=6, height=7, width=10, color=(200, 400, 222))
        # canvas.make("CANVAS.png")
        r1.draw(canvas)

    if user_input.lower() == 'square':
        square_x = int(input("\n enter x coordinate of square    "))
        square_y = int(input("\n enter y coordinate of square  "))
        square_side = int(input("\n enter side of rectangle  "))
        red = int(input("\nHow much red color you want, enter values between 0-255    "))
        green = int(input("\nHow much green color you want, enter values between 0-255    "))
        blue = int(input("\nHow much blue color you want, enter values between 0-255    "))
        Square1 = Square(x=square_x, y=square_y, side=square_side, color=(red,green,blue))

    if user_input.lower() == 'quit':
        break


canvas.make('CANVAS.png')