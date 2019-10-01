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

        objects.add(self)

    def remove(self):
        global objects

        for el in self.content:
            deleteObject(el)

        objects -= {self}

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


objects = set()

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

def create_dodik():
    global dodik

    content = list()

    body = (513, 761, 513 + 54, 761 + 117)
    content.append(c.create_oval(*body, fill='#dde9af', outline='#dde9af'))

    head = list()

    head.append((500, 699))
    head.append((499, 692))
    head.append((499, 686))
    head.append((500, 683))
    head.append((502, 680))
    head.append((507, 676))
    head.append((521, 678))
    head.append((541, 678))
    head.append((569, 675))
    head.append((580, 675))
    head.append((592, 678))
    head.append((605, 684))
    head.append((607, 687))
    head.append((607, 694))
    head.append((605, 704))
    head.append((599, 717))
    head.append((593, 727))
    head.append((584, 739))
    head.append((564, 760))
    head.append((556, 764))
    head.append((546, 764))
    head.append((536, 760))
    head.append((523, 748))
    head.append((518, 740))
    head.append((504, 710))

    head_outline = [(507, 709)] + head + [(496, 692)]


    penColor('#dde9af')
    brushColor('#dde9af')
    content.append(polygon(head))

    penColor('#090a06')
    content.append(polyline(head_outline))


    ovals = list()

    ovals.append((473, 609, 473 + 27, 609 + 22))
    ovals.append((479, 629, 479 + 21, 629 + 12))
    ovals.append((491, 642, 491 + 17, 642 + 20))
    ovals.append((502, 661, 502 + 10, 661 + 15))

    ovals.append((647, 633, 647 + 23, 633 + 28))
    ovals.append((626, 635, 626 + 15, 635 + 12))
    ovals.append((607, 643, 607 + 15, 643 + 16))
    ovals.append((602, 660, 602 + 8, 660 + 15))
    ovals.append((592, 667, 592 + 18, 667 + 18))

    ovals.append((481, 808, 481 + 11, 808 + 15))
    ovals.append((490, 789, 490 + 23, 789 + 17))
    ovals.append((501, 767, 501 + 28, 767 + 28))

    ovals.append((602, 794, 602 + 32, 794 + 17))
    ovals.append((575, 785, 575 + 27, 785 + 18))
    ovals.append((561, 770, 561 + 29, 770 + 29))

    ovals.append((471, 899, 471 + 28, 899 + 27))
    ovals.append((494, 872, 494 + 23, 872 + 47))
    ovals.append((498, 834, 498 + 29, 834 + 44))

    ovals.append((547, 851, 547 + 29, 851 + 42))
    ovals.append((558, 887, 558 + 21, 887 + 48))
    ovals.append((575, 915, 575 + 28, 915 + 27))


    for oval in ovals:
        content.append(c.create_oval(*oval, fill='#dde9af', outline='#dde9af'))

    dodik = Object(
    c.create_oval(514, 691, 514 + 35, 691 + 33, fill='black', outline='black'),
    c.create_oval(570, 698, 570 + 24, 698 + 26, fill='black', outline='black'),
    *content)

def create_eye1():
    global eye1

    obj = c.create_oval(531, 708, 531 + 9, 708 + 8, fill='white', outline='white')
    eye1 = Object(obj)

    eye1.pos1 = (xCoord(obj) + 1, yCoord(obj) + 1)
    eye1.pos2 = (514 + (35 - 9) // 2, 691 + (33 - 8) // 2)
    eye1.size = 9.5

def create_eye2():
    global eye2

    obj = c.create_oval(581, 711, 581 + 7, 711 + 7, fill='white', outline='white')
    eye2 = Object(obj)

    eye2.pos1 = (xCoord(obj) + 1, yCoord(obj) + 1)
    eye2.pos2 = (570 + (24 - 7) // 2, 698 + (26 - 7) // 2)
    eye2.size = 7


def create_apple():
    global apple

    content = list()
    content.append(
    c.create_oval(620, 751, 620 + 55, 751 + 53, fill='#c83737', outline='#c83737')
    )

    branch = list()

    branch.append((645, 755))
    branch.append((648, 751))
    branch.append((650, 747))
    branch.append((655, 741))
    branch.append((662, 733))

    content.append(polyline(branch))

    leave = list()

    leave.append((650, 748))
    leave.append((644, 743))
    leave.append((642, 738))
    leave.append((642, 727))
    leave.append((644, 727))
    leave.append((648, 733))
    leave.append((651, 739))
    leave.append((651, 747))

    brushColor('#88aa00')
    content.append(polygon(leave))

    apple = Object(*content, changing=animate_apple)

va_const = -8
g_const = 0.75

va = 0
g = 0
def animate_apple(i):
    global va, g

    dy = va + g // 2
    va += g

    for obj in apple.content:
        moveObjectBy(obj, 0, dy)


    if i == step * 2:
        va = va_const
        g = g_const

    sep = int(2 * abs(va_const / g_const) + 1)

    if i == sep + step * 2:
        va = 0
        g = 0

    if i == int(sep + 2.5 * step):
        va = va_const
        g = g_const

    if i == int(2 * sep + 2.5 * step):
        va = 0
        g = 0

        apple.remove()
        create_apple()

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
create_dodik()
create_eye1()
create_eye2()
create_apple()

onTimer(animation, int(fps * 1000 + 0.5))


run()
