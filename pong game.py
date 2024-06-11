import turtle
# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)


# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5


# Initialize the score
left_player = 0
right_player = 0


# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0 Right_player: 0",
			align="center", font=("Courier", 24, "normal"))


# Functions to move paddle vertically
def paddleaup():
	y = left_pad.ycor()
	y += 20
	left_pad.sety👍


def paddleadown():
	y = left_pad.ycor()
	y -= 20
	left_pad.sety👍


def paddlebup():
	y = right_pad.ycor()
	y += 20
	right_pad.sety👍


def paddlebdown():
	y = right_pad.ycor()
	y -= 20
	right_pad.sety👍


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")


while True:
	sc.update()

	hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

	# Checking borders
	if hit_ball.ycor() > 280:
		hit_ball.sety(280)
		hit_ball.dy *= -1

	if hit_ball.ycor() < -280:
		hit_ball.sety(-280)
		hit_ball.dy *= -1

	if hit_ball.xcor() > 500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		left_player += 1
		sketch.clear()
		sketch.write("Left_player : {} Right_player: {}".format(
					left_player, right_player), align="center",
					font=("Courier", 24, "normal"))

	if hit_ball.xcor() < -500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		right_player += 1
		sketch.clear()
		sketch.write("Left_player : {} Right_player: {}".format(
								left_player, right_player), align="center",
								font=("Courier", 24, "normal"))

	# Paddle ball collision
	if (hit_ball.xcor() > 360 and	hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40):
		hit_ball.setx(360)
		hit_ball.dx*=-1
		
	if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+40 and hit_ball.ycor()>left_pad.ycor()-40):
		hit_ball.setx(-360)
		hit_ball.dx*=-1

from turtle import Turtle, Screen
from ball import Ball
from score_board import Scoreboard
from paddle import Paddle
import time
screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.setup(width = 800,height = 600)


r_paddle = Paddle((350,0))#x = 350,y = 0
l_paddle = Paddle((-350,0))#x = -350,y=0
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_is_on = True
while game_is_on:
    #time.sleep(0.1)   #check once before explaining
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.ycor()>290 or ball.ycor() < -290:
        ball.bounce_y()
    #detect collision for both paddles
    if ball.distance(r_paddle)<50 and ball.xcor()>325 or ball.distance(l_paddle)<50 and ball.xcor()<-325:
        ball.bounce_x()
        
    #if r paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    #if l paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
    #win and lose
    if scoreboard.l_score==6:
        scoreboard.l_win()
        break
    if scoreboard.r_score == 6:
        scoreboard.r_win()
        break

screen.exitonclick()

#paddle
class Paddle(Turtle):
  def _init_(self,position):
    super()._init_()# paddle = Turtle()
    self.shape("square")
    self.color("white") #paddle.color("white")
    self.shapesize(stretch_wid=5,stretch_len=1)
    self.penup()# doesnt draw
    self.goto(position) #self.goto(x = xloc,y=yloc)
    
  def go_up(self):
    new_y = self.ycor()+30
    self.goto(self.xcor(),new_y)
    
  def go_down(self):
    new_y = self.ycor()-30
    self.goto(self.xcor(),new_y)

 #ball
class Ball(Turtle):
    def _init_ (self):
        super()._init_()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 1.7
        self.y_move = 1.7
    def move(self):
        new_x = self.xcor()+ self.x_move
        new_y=self.ycor()+ self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move *=-1 #reverses direction
    def bounce_x(self):
        self.x_move*=-1
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()

#scoreboard
from turtle import Turtle
class Scoreboard(Turtle):
    def _init_(self):
        super()._init_()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align = "center",font = ("courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score, align = "center",font = ("courier",80,"normal"))
    
    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()
