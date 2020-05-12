from tkinter import *
import time
import random

tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 120, text='Ты лох', font=('Courier', 30), fill='red')
            paddle.started = False
        if self.hit_paddle(pos):
            self.y = -1
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2


class Paddle:
    def __init__(self, canvas, color, width):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, width, 10, fill=color)
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(start_1)
        self.starting_point_x = start_1[0]
        self.canvas.move(self.id, self.starting_point_x, 300)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
        self.canvas.bind_all('<KeyRelease-Left>', self.turn_left_release)
        self.canvas.bind_all('<KeyRelease-Right>', self.turn_right_release)
        self.right = False
        self.left = False

    def turn_right(self, event):
        self.x = 3
        self.right = True

    def turn_left(self, event):
        self.x = -3
        self.left = True

    def turn_right_release(self, event):
        self.right = False

    def turn_left_release(self, event):
        self.left = False

    def start_game(self, event):
        self.started = True

    def draw(self):
        pos = self.canvas.coords(self.id)
        canvas_width = self.canvas.winfo_width()
        if pos[0] + self.x < 0:
            self.x = 0
            '''newpos = pos
            newpos[0] = 0
            newpos[2] = pos[2] + abs(newpos[0] - pos[0])
            canvas.coords(self.id, newpos)'''
        elif pos[2] + self.x >= canvas_width:
            self.x = 0
            '''newpos = pos
            newpos[2] = canvas_width - 1
            newpos[0] = pos[0] - (newpos[2] - pos[2])
            canvas.coords(self.id, newpos)'''
        self.canvas.move(self.id, self.x, 0)
        if self.x < 0 and self.left == False:
            self.x = 0
        if self.x > 0 and self.right == False:
            self.x = 0


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White', 100)
balls = [Ball(canvas, 'red')]
balls_flag = True
balls_count = 0
balls_score = [2, 5, 13]
while not sum([balls[i].hit_bottom for i in range(len(balls))]):
    if paddle.started:
        for i in range(len(balls)):
            balls[i].draw()
        if score.score == balls_score[balls_count] and balls_flag:
            balls.append(Ball(canvas, 'red'))
            balls_flag = False
            paddle_coords = paddle.canvas.coords(paddle.id)
            if paddle_coords[2] < (paddle.canvas.winfo_width() // 2):
                paddle_coords[2] += 30
            else:
                paddle_coords[0] -= 30
            paddle.canvas.coords(paddle.id, paddle_coords)
            if balls_count < 2:
                balls_count += 1
        if score.score == balls_score[balls_count] - 1:
            balls_flag = True
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    speed = score.score * 0.0002
    if speed > 0.0065: speed = 0.0065
    time.sleep(0.01 - speed)
time.sleep(3)
