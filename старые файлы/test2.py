from tkinter import *
import random
WIDTH = 800
HEIGHT = 600
seg_size = 20
IN_GAME = True

def main():
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords

        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False


        root.after(100, main)



def create_block():
    global BLOCK
    posx = seg_size * random.randint(1, (WIDTH - seg_size) / seg_size)
    posy = seg_size * random.randint(1, (HEIGHT - seg_size) / seg_size)
    BLOCK = c.create_oval(posx, posy,
                          posx + seg_size, posy + seg_size,
                          fill='green')

class Segment():
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + seg_size, y + seg_size,
                                           fill='green')

def create_snake():
    segments = [Segment(seg_size, seg_size),
                Segment(seg_size * 2, seg_size),
                Segment(seg_size * 3, seg_size)]
    return Snake(segments)

def startgame():
    global s
    create_block()
    s = create_snake()
    c.bind("<KeyPress>", s.change_direction)
    main()

"""У змеи будет много методов, поэтому оформляем как класс.
Сегменты тоже будут добавляться постоянно и с ними много операций, поэтому класс.
А вот корм как просто переменную создаваемую функцией.
Вызывая класс сегмент и создавай его экземпеляр
"""

class Snake(object):
    def __init__(self, segments):
        self.segments = segments
        self.mapping = {"DOWN": (0, 1), "up": (0, -1),
                        "RIGHT": (1, 0), "LEFT": (-1, 0)}

        self.vector = self.mapping["RIGHT"]

    def move(self):
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1],
                 x1 + self.vector[0] * seg_size, y1 + self.vector[1] * seg_size,
                 x2 + self.vector[0] * seg_size, y2 + self.vector[1] * seg_size)

    def add_segment(self):
        pass

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]


root = Tk()
root.title('Snake')
c = Canvas(root, width=WIDTH, height=HEIGHT, bg='#000000')
c.grid()
c.focus_set()
startgame()
root.mainloop()