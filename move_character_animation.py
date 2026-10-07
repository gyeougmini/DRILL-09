from pico2d import *

WIDTH, HEIGHT = 1280, 1024

FRAME_SIZE = 100
FRAME_COUNT = 8

# animation_sheet.png 행의 clip y 좌표 (아래쪽이 0)
IDLE_RIGHT = 300
IDLE_LEFT = 200
RUN_RIGHT = 100
RUN_LEFT = 0

SPEED = 5
FRAME_DELAY = 0.05
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


def update_character():
    global x, y, frame, face

    frame = (frame + 1) % FRAME_COUNT
    x = clamp(HALF_W, x + dir_x * SPEED, WIDTH - HALF_W)
    y = clamp(HALF_H, y + dir_y * SPEED, HEIGHT - HALF_H)
    # 상하로만 이동할 때는 마지막 좌우 방향을 유지한다
    if dir_x > 0:
        face = 1
    elif dir_x < 0:
        face = -1


def draw_character():
    if dir_x != 0 or dir_y != 0:
        row = RUN_RIGHT if face == 1 else RUN_LEFT
    else:
        row = IDLE_RIGHT if face == 1 else IDLE_LEFT
    character.clip_draw(frame * FRAME_SIZE, row, FRAME_SIZE, FRAME_SIZE, x, y)


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
    draw_character()
    update_canvas()
    handle_events()
    update_character()
    delay(FRAME_DELAY)

close_canvas()
