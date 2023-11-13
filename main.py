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

MARBLE_SPEED = 5

X_OFFSET = 0
Y_OFFSET = 0
ZOOM = 1

def is_visible(x, y):
    return (x - X_OFFSET) * ZOOM > 0 and (x - X_OFFSET) * ZOOM < WIDTH and (y - Y_OFFSET) * ZOOM > 0 and (y - Y_OFFSET) * ZOOM < HEIGHT

def get_x(x):
    return round((x - X_OFFSET) * ZOOM)

def get_y(y):
    return round((y - Y_OFFSET) * ZOOM)

def gen_color(x, y):
    return (x * 50 % 180, y * 50 % 180, (x + y) * 50 % 180)

class IO:
    def __init__(self, ptd_sw, index, current = None):
        self.ptd_sw = ptd_sw
        self.current_sw = current
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
                x = self.get_io_pos(i)
                y = x[1]
                x = x[0]
                pygame.draw.line(screen, gen_color(x, y), self.get_io_pos(i), self.io[i].ptd_sw.get_io_pos(self.io[i].index), round(2 * ZOOM))

    def toggle(self):
        self.active = not self.active

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
    
    def get_directed_out(self):
        if self.active:
            return self.io[2]
        else:
            return self.io[1]

class Marble:
    def __init__(self, color):
        self.color = color
        self.into = [None, None]
        self.traveled = 0
        self.length = 0
        self.name = "THE MARBLE"

    def draw(self):
        if self.into[0] is None:
            return
        x1 = self.into[0].ptd_sw.get_io_pos(self.into[0].index)[0]
        y1 = self.into[0].ptd_sw.get_io_pos(self.into[0].index)[1]
        if self.into[1] is None:
            pygame.draw.circle(screen, self.color, (x1, y1), round(5 * ZOOM))
            return
        x2 = self.into[1].ptd_sw.get_io_pos(self.into[1].index)[0]
        y2 = self.into[1].ptd_sw.get_io_pos(self.into[1].index)[1]
        x = x1 + (x2 - x1) * self.traveled / self.length
        y = y1 + (y2 - y1) * self.traveled / self.length
        pygame.draw.circle(screen, self.color, (x, y), round(5 * ZOOM))

    def move(self):
        if self.into[0] is None or self.into[1] is None:
            return
        if self.traveled == 0:
            self.length = ((get_x(self.into[0].ptd_sw.get_io_pos(self.into[0].index)[0]) - get_x(self.into[1].ptd_sw.get_io_pos(self.into[1].index)[0])) ** 2 + (get_y(self.into[0].ptd_sw.get_io_pos(self.into[0].index)[1]) - get_y(self.into[1].ptd_sw.get_io_pos(self.into[1].index)[1])) ** 2) ** 0.5
        self.traveled += MARBLE_SPEED
        if self.traveled > self.length:
            self.into[0] = self.into[1].ptd_sw.io[2 if self.into[1].ptd_sw.active else 1]
            self.into[1] = self.into[0].ptd_sw.io[self.into[0].index]
            (self.into[0], self.into[1]) = (self.into[1], self.into[0])
            if self.into[1] is None:
                print("MARBLE BAD SWITCH")
            print("MARBLE SWITCH")
            self.traveled = 0
            self.length = ((m.into[1].ptd_sw.x - m.into[0].ptd_sw.x) ** 2 + (m.into[1].ptd_sw.y - m.into[0].ptd_sw.y) ** 2) ** 0.5

mouse_down = [-1, -1]

s = [Switch(0, 0, "init")]
m = Marble((255, 0, 0))

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
                                crsw.io[i].ptd_sw.io[crsw.io[i].index] = None
                                crsw.io[i] = None
                        else:
                            if tmp_io is None:
                                tmp_io = IO(crsw, i)
                            else:
                                if tmp_io.ptd_sw is not crsw:
                                    if tmp_io.ptd_sw.io[tmp_io.index] is not None:
                                        print("delete old io")
                                        tmp_io.ptd_sw.io[tmp_io.index].ptd_sw.io[tmp_io.ptd_sw.io[tmp_io.index].index] = None
                                    if crsw.io[i] is not None:
                                        print("delete new io")
                                        crsw.io[i].ptd_sw.io[crsw.io[i].index] = None

                                    tmp_io.ptd_sw.io[tmp_io.index] = IO(crsw, i)
                                    crsw.io[i] = tmp_io
                                    print(tmp_io.ptd_sw.io[tmp_io.index].ptd_sw.name)
                                    print(crsw.io[i].ptd_sw.name)
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
                                    crsw.io[i].ptd_sw.io[crsw.io[i].index] = None
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
            elif event.key == pygame.K_l:
                # list all switches and their io
                print("switches:")
                for crsw in s:
                    print(crsw.name)
                    for i in range(3):
                        if crsw.io[i] is not None:
                            print(f"  {i}: {crsw.io[i].ptd_sw.name}")
                        else:
                            print(f"  {i}: None")
                # list all marbles
                print("marble:")
                print(f"  into[0]: {m.into[0].ptd_sw.name if m.into[0] is not None else None}")
                print(f"  into[1]: {m.into[1].ptd_sw.name if m.into[1] is not None else None}")
                print(f"  traveled: {m.traveled}")
                print(f"  length: {m.length}")


            elif event.key == pygame.K_r:
                for crsw in s:
                    if get_x(crsw.x) < pygame.mouse.get_pos()[0] < get_x(crsw.x) + 20 * ZOOM and get_y(crsw.y) < pygame.mouse.get_pos()[1] < get_y(crsw.y) + 20 * ZOOM:
                        crsw.rotate()
                        break
            elif event.key == pygame.K_m:
                for crsw in s:
                    if get_x(crsw.x) < pygame.mouse.get_pos()[0] < get_x(crsw.x) + 20 * ZOOM and get_y(crsw.y) < pygame.mouse.get_pos()[1] < get_y(crsw.y) + 20 * ZOOM:
                        print(f"set marble to {crsw.name}")
                        m.into[1] = crsw.get_directed_out()
                        if m.into[1] is not None:
                            m.into[0] = m.into[1].ptd_sw.io[m.into[1].index]
                            m.length = ((m.into[1].ptd_sw.x - m.into[0].ptd_sw.x) ** 2 + (m.into[1].ptd_sw.y - m.into[0].ptd_sw.y) ** 2) ** 0.5
                        else:
                            m.into[0] = None
                            m.length = 0
                        m.traveled = 0
                        break

    screen.fill((0, 0, 0))
    for switch in s:
        switch.draw()
    
    # move marble
    m.move()
    m.draw()


    # draw fps
    fps = f"fps: {int(clock.get_fps())} [{X_OFFSET}, {Y_OFFSET}] x{ZOOM}"

    font = pygame.font.SysFont("Arial", 15)
    fps_text = font.render(fps, True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.update()
    
    clock.tick(60)
