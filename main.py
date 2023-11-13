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

class IO:
    def __init__(self, switch, index):
        self.switch = switch
        self.index = index

class Switch:
    def __init__(self, x, y, name = ""):
        self.x = x
        self.y = y
        self.active = False
        self.rotation = 1 # 0 = up, 1 = right, 2 = down, 3 = left
        self.io = [None, None, None]
        self.name = name

    def get_io_pos(self, index):
        if self.rotation == 0:
            if index == 0:
                return (get_x(self.x) + 10 * ZOOM, get_y(self.y) + 20 * ZOOM)
            elif index == 1:
                return (get_x(self.x) + ZOOM * 2, get_y(self.y))
            elif index == 2:
                return (get_x(self.x) + 18 * ZOOM, get_y(self.y))
        elif self.rotation == 1:
            if index == 0:
                return (get_x(self.x), get_y(self.y) + 10 * ZOOM)
            elif index == 1:
                return (get_x(self.x) + 20 * ZOOM, get_y(self.y) + ZOOM * 2)
            elif index == 2:
                return (get_x(self.x) + 20 * ZOOM, get_y(self.y) + 18 * ZOOM)
        elif self.rotation == 2:
            if index == 0:
                return (get_x(self.x) + 10 * ZOOM, get_y(self.y))
            elif index == 1:
                return (get_x(self.x) + ZOOM * 2, get_y(self.y) + 20 * ZOOM)
            elif index == 2:
                return (get_x(self.x) + 18 * ZOOM, get_y(self.y) + 20 * ZOOM)
        elif self.rotation == 3:
            if index == 0:
                return (get_x(self.x) + 20 * ZOOM, get_y(self.y) + 10 * ZOOM)
            elif index == 1:
                return (get_x(self.x), get_y(self.y) + ZOOM * 2)
            elif index == 2:
                return (get_x(self.x), get_y(self.y) + 18 * ZOOM)

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

        # draw io
        for i in range(3):
            if self.io[i] is not None:
                pygame.draw.line(screen, SWITCH_COLOR_IO, self.get_io_pos(i), self.io[i].switch.get_io_pos(self.io[i].index), round(2 * ZOOM))

    def toggle(self):
        self.active = not self.active

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

mouse_down = [-1, -1]

s = [Switch(0, 0, "init")]
tmp_io = None

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
            found = False
            for crsw in s:
                # check if mouse is on IO
                for i in range(3):
                    io = crsw.get_io_pos(i)
                    if io[0] - 5 * ZOOM < pygame.mouse.get_pos()[0] < io[0] + 5 * ZOOM and io[1] - 5 * ZOOM < pygame.mouse.get_pos()[1] < io[1] + 5 * ZOOM:
                        found = True
                        if event.button == 3: # delete io
                            if crsw.io[i] is not None:
                                crsw.io[i].switch.io[crsw.io[i].index] = None
                                crsw.io[i] = None
                        else:
                            if tmp_io is None:
                                tmp_io = IO(crsw, i)
                            else:
                                if tmp_io.switch is not crsw:
                                    if tmp_io.switch.io[tmp_io.index] is not None:
                                        print("delete old io")
                                        tmp_io.switch.io[tmp_io.index].switch.io[tmp_io.switch.io[tmp_io.index].index] = None
                                    if crsw.io[i] is not None:
                                        print("delete new io")
                                        crsw.io[i].switch.io[crsw.io[i].index] = None

                                    tmp_io.switch.io[tmp_io.index] = IO(crsw, i)
                                    crsw.io[i] = tmp_io
                                    print(tmp_io.switch.io[tmp_io.index].switch.name)
                                    print(crsw.io[i].switch.name)
                                    tmp_io = None
                                else:
                                    print("same switch")
                                    tmp_io.index = i
                        break
                else:
                    if get_x(crsw.x) < pygame.mouse.get_pos()[0] < get_x(crsw.x) + 20 * ZOOM and get_y(crsw.y) < pygame.mouse.get_pos()[1] < get_y(crsw.y) + 20 * ZOOM:
                        print(f"switch clicked {crsw.name}")
                        found = True
                        if event.button == 3:
                            for i in range(3):
                                if crsw.io[i] is not None:
                                    crsw.io[i].switch.io[crsw.io[i].index] = None
                            s.remove(crsw)
                        else:
                            crsw.toggle()
                        break

            if not found:
                if event.button == 3:
                    s.append(Switch(round((pygame.mouse.get_pos()[0]) / ZOOM + X_OFFSET, 1), round((pygame.mouse.get_pos()[1]) / ZOOM + Y_OFFSET, 1), str(len(s))))

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
            if event.key == pygame.K_x:
                X_OFFSET = 0
                Y_OFFSET = 0
                ZOOM = 1
            if event.key == pygame.K_l:
                # list all switches and their io
                print("switches:")
                for crsw in s:
                    print(crsw.name)
                    for i in range(3):
                        if crsw.io[i] is not None:
                            print(f"  {i}: {crsw.io[i].switch.name}")
                        else:
                            print(f"  {i}: None")
            if event.key == pygame.K_r:
                for crsw in s:
                    if get_x(crsw.x) < pygame.mouse.get_pos()[0] < get_x(crsw.x) + 20 * ZOOM and get_y(crsw.y) < pygame.mouse.get_pos()[1] < get_y(crsw.y) + 20 * ZOOM:
                        crsw.rotate()
                        break

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
