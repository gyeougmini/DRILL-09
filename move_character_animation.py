from pico2d import *

WIDTH, HEIGHT = 1280, 1024

# animation_sheet.png 행의 clip y 좌표 (아래쪽이 0)
IDLE_RIGHT = 300
IDLE_LEFT = 200
RUN_RIGHT = 100
RUN_LEFT = 0

SPEED = 5


def handle_events():
    global running, dir_x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                dir_x += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                dir_x -= 1


open_canvas(WIDTH, HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
dir_x = 0

while running:
    clear_canvas()
    ground.draw(WIDTH // 2, HEIGHT // 2)
    character.clip_draw(frame * 100, IDLE_RIGHT, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * SPEED
    delay(0.05)

close_canvas()
