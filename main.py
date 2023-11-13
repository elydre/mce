import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MCE")
clock = pygame.time.Clock()

SWITCH_COLOR_ON = (169, 73, 82)
SWITCH_COLOR_OFF = (99, 129, 135)
SWITCH_COLOR_IO = (230, 235, 237)
SWITCH_COLOR_BAR = (0, 0, 0)

X_OFFSET = 0
Y_OFFSET = 0
ZOOM = 1

def is_visible(x, y):
    return (x - X_OFFSET) * ZOOM > 0 and (x - X_OFFSET) * ZOOM < WIDTH and (y - Y_OFFSET) * ZOOM > 0 and (y - Y_OFFSET) * ZOOM < HEIGHT

def get_x(x):
    return round((x - X_OFFSET) * ZOOM)

def get_y(y):
    return round((y - Y_OFFSET) * ZOOM)

class Switch:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = False
        self.rotation = 1 # 0 = up, 1 = right, 2 = down, 3 = left
    
    def draw(self):
        # check if switch is visible
        if not is_visible(self.x, self.y) and not is_visible(self.x + 20, self.y + 20):
            return

        # draw switch
        if self.active:
            pygame.draw.rect(screen, SWITCH_COLOR_ON, (get_x(self.x), get_y(self.y), 20 * ZOOM, 20 * ZOOM))
        else:
            pygame.draw.rect(screen, SWITCH_COLOR_OFF, (get_x(self.x), get_y(self.y), 20 * ZOOM, 20 * ZOOM))

        # draw io and active bar
        # one input under the switch (use rotation)
        # tow outputs on the top corners (use rotation)
        # active bar from bottom to left corner if not active else from top to right corner
        if self.rotation == 0:
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) + 5 * ZOOM, get_y(self.y) + 20 * ZOOM, 10 * ZOOM, 5 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x), get_y(self.y) - 5 * ZOOM, 5 * ZOOM, 5 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) + 15 * ZOOM, get_y(self.y) - 5 * ZOOM, 5 * ZOOM, 5 * ZOOM))
            if self.active:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x) + 10 * ZOOM, get_y(self.y) + 20 * ZOOM), (get_x(self.x) + 18 * ZOOM, get_y(self.y)), round(2 * ZOOM))
            else:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x) + 10 * ZOOM, get_y(self.y) + 20 * ZOOM), (get_x(self.x) + ZOOM * 2, get_y(self.y)), round(2 * ZOOM))

        elif self.rotation == 1:
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) - 5 * ZOOM, get_y(self.y) + 5 * ZOOM, 5 * ZOOM, 10 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) + 20 * ZOOM, get_y(self.y), 5 * ZOOM, 5 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) + 20 * ZOOM, get_y(self.y) + 15 * ZOOM, 5 * ZOOM, 5 * ZOOM))
            if self.active:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x), get_y(self.y) + 10 * ZOOM), (get_x(self.x) + 20 * ZOOM, get_y(self.y) + 18 * ZOOM), round(2 * ZOOM))
            else:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x), get_y(self.y) + 10 * ZOOM), (get_x(self.x) + 20 * ZOOM, get_y(self.y) + ZOOM * 2), round(2 * ZOOM))
        elif self.rotation == 2:
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) + 5 * ZOOM, get_y(self.y) - 5 * ZOOM, 10 * ZOOM, 5 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x), get_y(self.y) + 20 * ZOOM, 5 * ZOOM, 5 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) + 15 * ZOOM, get_y(self.y) + 20 * ZOOM, 5 * ZOOM, 5 * ZOOM))
            if self.active:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x) + 10 * ZOOM, get_y(self.y)), (get_x(self.x) + 18 * ZOOM, get_y(self.y) + 20 * ZOOM), round(2 * ZOOM))
            else:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x) + 10 * ZOOM, get_y(self.y)), (get_x(self.x) + ZOOM * 2, get_y(self.y) + 20 * ZOOM), round(2 * ZOOM))
        elif self.rotation == 3:
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) + 20 * ZOOM, get_y(self.y) + 5 * ZOOM, 5 * ZOOM, 10 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) - 5 * ZOOM, get_y(self.y), 5 * ZOOM, 5 * ZOOM))
            pygame.draw.rect(screen, SWITCH_COLOR_IO, (get_x(self.x) - 5 * ZOOM, get_y(self.y) + 15 * ZOOM, 5 * ZOOM, 5 * ZOOM))
            if self.active:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x) + 20 * ZOOM, get_y(self.y) + 10 * ZOOM), (get_x(self.x), get_y(self.y) + 18 * ZOOM), round(2 * ZOOM))
            else:
                pygame.draw.line(screen, SWITCH_COLOR_BAR, (get_x(self.x) + 20 * ZOOM, get_y(self.y) + 10 * ZOOM), (get_x(self.x), get_y(self.y) + ZOOM * 2), round(2 * ZOOM))

    def toggle(self):
        self.active = not self.active

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

mouse_down = [-1, -1]

s = [Switch(0, 0)]

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # ZOOM IN/OUT
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            old_zoom = ZOOM
            ZOOM = round(ZOOM + 0.1, 1)
            X_OFFSET = round(X_OFFSET + (WIDTH / 2) / old_zoom - (WIDTH / 2) / ZOOM, 1)
            Y_OFFSET = round(Y_OFFSET + (HEIGHT / 2) / old_zoom - (HEIGHT / 2) / ZOOM, 1)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            old_zoom = ZOOM
            ZOOM = max(round(ZOOM - 0.1, 1), 0.1)
            X_OFFSET = round(X_OFFSET + (WIDTH / 2) / old_zoom - (WIDTH / 2) / ZOOM, 1)
            Y_OFFSET = round(Y_OFFSET + (HEIGHT / 2) / old_zoom - (HEIGHT / 2) / ZOOM, 1)

        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN and event.button in [1, 3]:
            # check if switch is clicked
            for switch in s:
                if get_x(switch.x) < pygame.mouse.get_pos()[0] < get_x(switch.x) + 20 * ZOOM and get_y(switch.y) < pygame.mouse.get_pos()[1] < get_y(switch.y) + 20 * ZOOM:
                    if event.button == 3:
                        switch.rotate()
                    else:
                        switch.toggle()
                    break
                    
            if event.button == 1:
                mouse_down = pygame.mouse.get_pos()


        if event.type == pygame.MOUSEMOTION and mouse_down[0] != -1:
            # claculate offset
            mouse_new = pygame.mouse.get_pos()
            X_OFFSET = round(X_OFFSET + (mouse_down[0] - mouse_new[0]) / ZOOM, 1)
            Y_OFFSET = round(Y_OFFSET + (mouse_down[1] - mouse_new[1]) / ZOOM, 1)
            mouse_down = mouse_new
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_down = [-1, -1]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                X_OFFSET = 0
                Y_OFFSET = 0
                ZOOM = 1

    screen.fill((0, 0, 0))
    for switch in s:
        switch.draw()

    # draw fps
    fps = f"fps: {int(clock.get_fps())} [{X_OFFSET}, {Y_OFFSET}] x{ZOOM}"

    font = pygame.font.SysFont("Arial", 15)
    fps_text = font.render(fps, True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.update()
    
    clock.tick(60)
