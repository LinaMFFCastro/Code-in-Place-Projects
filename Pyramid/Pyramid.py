from graphics import Canvas
from numpy import random


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels


BRICK_WIDTH = 10        # The width of each brick in pixels
BRICK_HEIGHT = 10       # The height of each brick in pixels
BRICKS_IN_BASE = 20     # The number of bricks in the base


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


    for j in range(BRICKS_IN_BASE):
        for i in range(BRICKS_IN_BASE-j):
            start_x = (CANVAS_WIDTH-((BRICKS_IN_BASE-j)*BRICK_WIDTH))/2+BRICK_WIDTH*i
            start_y = CANVAS_HEIGHT - BRICK_HEIGHT*(j+1)
            end_x = (CANVAS_WIDTH-((BRICKS_IN_BASE-j)*BRICK_WIDTH))/2+(BRICK_WIDTH*(i+1))
            end_y = CANVAS_HEIGHT-BRICK_HEIGHT*j
            canvas.create_rectangle(start_x, start_y, end_x, end_y, 'yellow', 'black')

if __name__ == '__main__':
    main()
