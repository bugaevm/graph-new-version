from graph import *
from time import sleep

c = canvas()

width = 794
height = 1123

windowSize(width, height)
canvasSize(width, height)

fps = 1 / 60
step = int(1 / fps / 2)  # a half of a second
per = 16


def passing(*args):
    pass

class Object:
    def __init__(self, *args, changing=passing):
        global objects

        self.content = args
        self.change = changing

        objects.append(self)

    def remove(self):
        global objects

        for el in self.content:
            deleteObject(el)

        objects.pop(objects.index(self))

def html_col(col):
    r, g, b = col

    r = ('0' + hex(r)[2:])[-2:]
    g = ('0' + hex(g)[2:])[-2:]
    b = ('0' + hex(b)[2:])[-2:]

    return '#' + r + g + b

def change_col(col1, col2, i, length):
    r1, g1, b1 = col1
    r2, g2, b2 = col2

    r = r1 + int((r2 - r1) * (i + 1) / length + 0.5)
    g = g1 + int((g2 - g1) * (i + 1) / length + 0.5)
    b = b1 + int((b2 - b1) * (i + 1) / length + 0.5)

    return html_col((r, g, b))


objects = list()

def create_background():
    global background

    sky_col = (0, 34, 43)  #00222b
    horizon_col = (46, 69, 68)  #2e4544
    ground_col = (34, 43, 0)  #222b00

    penColor(horizon_col)
    brushColor(sky_col)
    penSize(1)

    a = rectangle(-1, -1, width + 1, 576)

    brushColor(ground_col)
    b = rectangle(-1, 576 + 1, width + 1, height + 1)

    background = Object(a, b)

    background.sky_col = sky_col
    background.horizon_col = horizon_col
    background.ground_col = ground_col

def create_sun():
    global sun

    penColor('#f2f2f2')
    brushColor('#f2f2f2')

    sun = Object(circle((631 + 383) // 2, (127 + 370) // 2, (631 - 383) // 2))

def create_clouds():
    global clouds

    light = list()
    dark = list()

    light.append((502, -22, 502 + 581, -22 + 116))
    light.append((-539, 16, -539 + 1035, 16 + 204))
    light.append((353, 142, 353 + 735, 142 + 125))
    light.append((-423, 245, -423 + 935, 245 + 131))
    light.append((260, 292, 260 + 756, 292 + 130))

    dark.append((137, 83, 137 + 739, 83 + 125))
    dark.append((-301, 214, -301 + 636, 214 + 123))
    dark.append((113, 379, 113 + 748, 379 + 121))

    objs = list()

    for cloud in light:
        objs.append(c.create_oval(*cloud, fill='#666666', outline='#666666'))

    for cloud in dark:
        objs.append(c.create_oval(*cloud, fill='#333333', outline='#333333'))

    clouds = Object(*objs)

def create_ray():
    global ray

    sky_col = (106, 125, 131)  #6a7d83
    horizon_col = (132, 146, 145)  #849291
    ground_col = (125, 131, 106)  #7d836a

    down = list()
    top = list()

    down.append((20, 734))
    down.append((344, 738))
    down.append((254, 578))
    down.append((93, 578))

    top.append((95, 575))
    top.append((252, 575))
    top.append((214, 508))
    top.append((128, 507))


    penColor(ground_col)
    brushColor(ground_col)
    r_down = polygon(down)

    penColor(sky_col)
    brushColor(sky_col)
    r_top = polygon(top)

    penColor(horizon_col)
    brushColor(horizon_col)
    r_hor = polygon([(94, 576), (253, 576), (254, 577), (93, 577)])

    ray = Object(r_down, r_hor, r_top, changing=animate_ray)

    ray.sky_col = sky_col
    ray.horizon_col = horizon_col
    ray.ground_col = ground_col

def animate_ray(i):
    if i // step == 7:
        j = i - 7 * step
        turn_off_ray(j)

    elif i == 8 * step:
        changeFillColor(ray.content[2], html_col(background.sky_col))
        changePenColor(ray.content[2], html_col(background.sky_col))

        changeFillColor(ray.content[1], html_col(background.horizon_col))
        changePenColor(ray.content[1], html_col(background.horizon_col))

        changeFillColor(ray.content[0], html_col(background.ground_col))
        changePenColor(ray.content[0], html_col(background.ground_col))

    elif i // step == 14:
        turn_on_ray(i - 14 * step)

def turn_off_ray(j):
    changeFillColor(ray.content[2], change_col(ray.sky_col, background.sky_col, j, step))
    changePenColor(ray.content[2], change_col(ray.sky_col, background.sky_col, j, step))

    changeFillColor(ray.content[1], change_col(ray.horizon_col, background.horizon_col, j, step))
    changePenColor(ray.content[1], change_col(ray.horizon_col, background.horizon_col, j, step))

    changeFillColor(ray.content[0], change_col(ray.ground_col, background.ground_col, j, step))
    changePenColor(ray.content[0], change_col(ray.ground_col, background.ground_col, j, step))

def turn_on_ray(j):
    changeFillColor(ray.content[2], change_col(background.sky_col, ray.sky_col, j, step))
    changePenColor(ray.content[2], change_col(background.sky_col, ray.sky_col, j, step))

    changeFillColor(ray.content[1], change_col(background.horizon_col, ray.horizon_col, j, step))
    changePenColor(ray.content[1], change_col(background.horizon_col, ray.horizon_col, j, step))

    changeFillColor(ray.content[0], change_col(background.ground_col, ray.ground_col, j, step))
    changePenColor(ray.content[0], change_col(background.ground_col, ray.ground_col, j, step))

def create_ufo():
    global ufo

    windows = list()

    windows.append((24, 443, 24 + 41, 443 + 18))
    windows.append((68, 464, 68 + 41, 464 + 18))
    windows.append((126, 474, 126 + 41, 474 + 18))
    windows.append((190, 476, 190 + 41, 476 + 18))
    windows.append((247, 465, 247 + 41, 465 + 18))
    windows.append((303, 444, 303 + 41, 444 + 18))

    content = list()

    content.append(c.create_oval(
        6, 393, 6 + 355, 393 + 117, fill='#999999', outline='#999999'
    ))

    content.append(c.create_oval(
        56, 383, 56 + 256, 383 + 82, fill='#cccccc', outline='#cccccc'
    ))

    for window in windows:
        content.append(c.create_oval(
            *window, fill='#ffffff', outline='#ffffff'
        ))

    ufo = Object(*content, changing=animate_ufo)

vy = 0
a = 0
vx = 0

def animate_ufo(i):
    global vx, vy, a

    dy = vy + a // 2
    vy += a
    dx = vx

    for obj in ufo.content:
        moveObjectBy(obj, dx, -dy)

    if i // step == 9:
        a = 0.75
        vx = 27

    elif i == 11 * step:
        ry1 = 0.5 * a * (2 * step) ** 2
        a = 3
        vy = -a * 2 * step

        rx = vx * 2 * step
        ry2 = 0.5 * a * (2 * step) ** 2
        for obj in ufo.content:
            moveObjectBy(obj, -rx, ry1 - ry2)
        vx = 0

    elif i == int(13.24 * step):
        a = 0
        vy = 0
        vx = 0

        ufo.remove()
        create_ufo()

i = 1
def animation():
    global i

    i += 1
    i %= 15 * step

    for obj in objects:
        obj.change(i)


create_background()
create_sun()
create_clouds()
create_ray()
create_ufo()
# create_dodik()
# create_apple()

onTimer(animation, int(fps * 1000 + 0.5))


run()
