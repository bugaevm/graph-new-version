from graph import *

c = canvas()

width = 794
height = 1123

windowSize(width, height)
canvasSize(width, height)

def create_background():
    penColor('#2e4544')
    brushColor('#00222b')
    penSize(1)

    rectangle(-1, -1, width + 1, 576)

    brushColor('#222b00')
    rectangle(-1, 576 + 1, width + 1, height + 1)


def create_sun():
    penColor('#f2f2f2')
    brushColor('#f2f2f2')

    circle((631 + 383) // 2, (127 + 370) // 2, (631 - 383) // 2)

def create_clouds():
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

    for cloud in light:
        c.create_oval(*cloud, fill='#666666', outline='#666666')

    for cloud in dark:
        c.create_oval(*cloud, fill='#333333', outline='#333333')


def create_ray():
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


    penColor('#7d836a')
    brushColor('#7d836a')
    polygon(down)

    penColor('#6a7d83')
    brushColor('#6a7d83')
    polygon(top)

    penColor('#849291')
    line(94, 576, 253, 576)
    line(93, 577, 254, 577)

def create_ufo():
    windows = list()

    windows.append((24, 443, 24 + 41, 443 + 18))
    windows.append((68, 464, 68 + 41, 464 + 18))
    windows.append((126, 474, 126 + 41, 474 + 18))
    windows.append((190, 476, 190 + 41, 476 + 18))
    windows.append((247, 465, 247 + 41, 465 + 18))
    windows.append((303, 444, 303 + 41, 444 + 18))

    c.create_oval(6, 393, 6 + 355, 393 + 117, fill='#999999', outline='#999999')
    c.create_oval(56, 383, 56 + 256, 383 + 82, fill='#cccccc', outline='#cccccc')

    for window in windows:
        c.create_oval(*window, fill='#ffffff', outline='#ffffff')







create_background()
create_sun()
create_clouds()
create_ray()
create_ufo()


run()
