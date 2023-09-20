from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')



def move_rect():
    x = 450
    y = 0
    while(x< 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x+2
        delay(0.01)
        
    while(y < 450):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(780,90 + y)
        y =  y+2
        delay(0.01)

    while(x > 20) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,540)
        x = x-2
        delay(0.01)

    while(y > 90) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(20,y)
        y =  y-2
        delay(0.01)

    while(x < 400) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x =  x+2
        delay(0.01)
 
def move_round():
    theta = 270
    x = 0
    y = 0
    while(theta < 360) :
        x = (210 * math.cos(math.radians(theta)))
        y = (210 * math.sin(math.radians(theta)))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+x,300+y)
        theta = theta + 2
        delay(0.01)
    theta = 0
    while(theta < 270) :
        x = (210 * math.cos(math.radians(theta)))
        y = (210 * math.sin(math.radians(theta)))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+x,300+y)
        theta = theta + 2
        delay(0.01)
   
for x in range(0,450,2):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        delay(0.01)
while(1) :     
    move_rect()
    move_round()
    


close_canvas()
