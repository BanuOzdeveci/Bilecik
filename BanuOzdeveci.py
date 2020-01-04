#Turtle Graphics Game
import turtle
import math
import random


#set up screen
screen=turtle.Screen()
screen.bgcolor("lightpink")
screen.tracer(2)

#draw border
myborder=turtle.Turtle()
myborder.penup()
myborder.setposition(-800,-800)
myborder.pendown()
myborder.pensize(7)
myborder.color("yellow")
myborder.speed(15)


for side in range(4):
    myborder.forward(1600)
    myborder.left(90)
myborder.hideturtle()




#create player1
player1=turtle.Turtle()
player1.color("purple")
player1.shape("turtle")
player1.penup()
player1.speed(1)
player1.shapesize(4)
player1.setposition(0,-200)


#create player 2
player2=turtle.Turtle()
player2.shapesize(4)
player2.color("blue")
player2.shape("turtle")
player2.penup()
player2.speed(1)
player2.setposition(0,-760)
player2.setheading(90)

player2speed=40

#move the player2 left and right

def move_left():
    x=player2.xcor()
    x-=player2speed
    if x<-750:
       x=-750
    player2.setx(x)
    

def move_right():
    x=player2.xcor()
    x+=player2speed
    if x>+750:
       x=+750
    player2.setx(x)

#create player 2's bullet


bullet=turtle.Turtle()
bullet.shapesize(3,3)
bullet.color("black")
bullet.shape("arrow")
bullet.penup()
bullet.speed(5)
bullet.setheading(90)
bullet.setposition(0,50)
bullet.hideturtle()


bulletspeed=50
  
    
    
#define bullet state
#ready-ready to fire
#fire-bullet is firing
bulletstate="ready"

def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    
    if bulletstate=="ready":
        bulletstate="fire"
  
    #move the bullet to the just above the player2
        x=player2.xcor()
        y=player2.ycor()+35
        bullet.setposition(x,y)
        bullet.showturtle()
        
        
def iscollision(goals,bullet):
     d1=math.sqrt(math.pow(goals.xcor()-bullet.xcor(),2)+ math.pow(goals.ycor()-bullet.ycor(),2))
     if d1<40:
       return True
       
     else:
       return False
    
    
    
#Set keyboard bindings
turtle.listen()
turtle.onkey(move_left,"a")
turtle.onkey(move_right,"d")
turtle.onkey(fire_bullet,"space")
    
    

#create goals
maxGoals=6
goals=[]

#create the score variable
score=0
for count in range(maxGoals):
 
    goals.append(turtle.Turtle())
    goals[count].color("green")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-800,800),random.randint(-800,800))
    goals[count].shapesize(3)


#set speed variable
speed=1


#define fonctions
def turnleft1():
    player1.left(30)
 
    
def turnright1():
    player1.right(30)


def increasespeed():
    global speed
    speed+=1
   
def iscollision(t1,t2):
     d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor()-t2.ycor(),2))
     if d<40:
       return True
       
     else:
       return False
    



       
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft1,"Left")
turtle.onkey(turnright1,"Right")
turtle.onkey(increasespeed,"Up")



while True:
    player1.forward(speed)
    

    #Border cheking
    if player1.xcor()>800 or player1.xcor()<-800:
        player1.right(180)
   
    if player1.ycor()>800 or player1.ycor()<-800:
        player1.right(180)
    
    

    
   
   
    #move the goal
    for count in range(maxGoals):
        goals[count].forward(3)
   
         #border checking

        if goals[count].xcor()>800 or goals[count].xcor()<-800:
            goals[count].right(270)
       
        if goals[count].ycor()>800 or goals[count].ycor()<-800:
            goals[count].right(270)
           
       #collision  checking for player1
        if iscollision(player1,goals[count]):
            goals[count].setposition(random.randint(-800,800),random.randint(-800,800))
            goals[count].right(random.randint(0,360))
