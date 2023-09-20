from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

def move_rect() :
    for x in range(400, 782, 2) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 90)
        delay(0.01)
    for y in range(90, 562, 2) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(780, y)
        delay(0.01)
    for x in range(780, 20, -2) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 560)
        delay(0.01)
    for y in range(560, 92, -2) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(20, y)
        delay(0.01)
    for x in range(20, 402, 2) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 90)
        delay(0.01)

def move_round() :
    for theta in range(270, 361, 1) :
        x = 210 * math.cos(math.radians(theta))
        y = 210 * math.sin(math.radians(theta))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x+400,y+300)
        delay(0.01)

    for theta in range(0, 271, 1) :
        x = 210 * math.cos(math.radians(theta))
        y = 210 * math.sin(math.radians(theta))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x+400,y+300)
        delay(0.01)
    
while(1) :
    move_rect()
    move_round()


close_canvas()
