from pico2d import *

WIDTH, HEIGHT = 1280, 1024

open_canvas(WIDTH, HEIGHT)

running = True

while running:
    clear_canvas()
    update_canvas()
    delay(0.05)

close_canvas()
