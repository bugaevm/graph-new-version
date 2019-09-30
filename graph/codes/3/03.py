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


def passing():
    pass

class Object:
    def __init__(self, *args, changing=passing):
        global objects

        self.content = list()

        for el in args:
            func, pars = el
            self.content.append(func(*pars))

        self.change = changing

        objects.append(self)

    def remove(self):
        for el in self.content:
            deleteObject(el)



objects = list()

i = 0
def animation():
    global i

    i += 1
    i %= 15 * step

    for obj in objects:
        obj.change(i)


onTimer(animation, int(fps * 1000 + 0.5))


run()
