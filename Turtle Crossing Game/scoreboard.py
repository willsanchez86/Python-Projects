from turtle import Turtle
ALIGNMENT = 'left'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.goto(-260, 260)
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f'Score: {self.level}', align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write('GAME OVER', align='center', font=FONT)