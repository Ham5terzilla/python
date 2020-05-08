from tkinter import *
import time
from random import *

tk = Tk()
tk.title('Game')
tk.resizable(0, 0)  # Запрет изменения размера окна
tk.wm_attributes('-topmost', 1)  # Атрибуты переданные в виртуальную машину. В данном случае, поверх окон
canvas = Canvas(tk, width=600, height=400)
canvas.pack()  # У каждого видимого элемента будут свои координати (что?)
tk.update()  # Обновление окна с холстом


class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # Делаем овэльного
        self.canvas.move(self, 245, 100)  # Помещает шарик в точку координат
        starts = [-2, -1, 1, 2]  # Список возможных направлений
        shuffle(starts)  # Тасуем
        self.x = starts[0]
        self.y = -2  # Изначально шар падает
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()  # Увеличивает счётчик.
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # Передвижение шарика на заданный вектор по заданному значению
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
            if pos[3] >= self.canvas_height:
                self.hit_bottom=True
                canvas.create_text(250, 120, text="Defeat", font=('Courier', 30), fill="green")
            if self.hit_paddle(pos) == True:
                self.y = -2
            if pos[0] <= 0:
                self.x = 2
            if pos[2]>=self.canvas_width:
                self.x = -2