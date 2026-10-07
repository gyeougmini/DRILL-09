from pico2d import *

WIDTH, HEIGHT = 1280, 1024

# animation_sheet.png 행의 clip y 좌표 (아래쪽이 0)
IDLE_RIGHT = 300
IDLE_LEFT = 200
RUN_RIGHT = 100
RUN_LEFT = 0

SPEED = 5
# 프레임 중심에서 실제 캐릭터 외곽까지의 거리 (전체 프레임 기준 최대값)
HALF_W = 34
HALF_H = 43


def handle_events():
    global running, dir_x, dir_y

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
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


open_canvas(WIDTH, HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
dir_x, dir_y = 0, 0
face = 1  # 1: 오른쪽, -1: 왼쪽

while running:
    clear_canvas()
    ground.draw(WIDTH // 2, HEIGHT // 2)
    if dir_x != 0 or dir_y != 0:
        row = RUN_RIGHT if face == 1 else RUN_LEFT
    else:
        row = IDLE_RIGHT if face == 1 else IDLE_LEFT
    character.clip_draw(frame * 100, row, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * SPEED
    y += dir_y * SPEED
    x = clamp(HALF_W, x, WIDTH - HALF_W)
    y = clamp(HALF_H, y, HEIGHT - HALF_H)
    if dir_x > 0:
        face = 1
    elif dir_x < 0:
        face = -1
    delay(0.05)

close_canvas()
