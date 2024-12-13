#This function draws a square using a 'for' loop and passing in the size as an argument
def draw_square(size):
    for i in range (size):
        print("#" * size)
draw_square(7)

print (" ") #I printed a space to separate the shapes for visual purposes

#To create a triangle I changed the function name for clarity and multiplied # by i
def draw_triangle(size):
    for i in range (size):
        print("#" * i)

draw_triangle(7)