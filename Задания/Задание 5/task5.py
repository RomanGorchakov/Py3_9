#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def move_ball_to(event):
    target_x = event.x
    target_y = event.y
    move_ball(target_x, target_y)


def move_ball(target_x, target_y):
    current_coords = c.coords(ball)
    current_x = (current_coords[0] + current_coords[2]) / 2
    current_y = (current_coords[1] + current_coords[3]) / 2

    step_x = (target_x - current_x) / 20
    step_y = (target_y - current_y) / 20

    c.move(ball, step_x, step_y)

    if abs(target_x - current_x) > abs(step_x) or \
       abs(target_y - current_y) > abs(step_y):
        root.after(20, move_ball, target_x, target_y)


if __name__ == '__main__':
    root = Tk()
    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()

    ball = c.create_oval(0, 100, 40, 140, fill='green')

    c.bind("<Button-1>", move_ball_to)

    root.mainloop()