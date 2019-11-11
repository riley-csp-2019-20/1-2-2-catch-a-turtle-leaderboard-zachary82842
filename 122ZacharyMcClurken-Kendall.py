# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

#-----game configuration----
turtleshape = "turtle"
turtlesize = 2.5
turtlecolor = "green"
score = 0

timer = 18
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#Scoreboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name.")


#colors to pick from
color_list = ["white", "orange", "purple", "yellow", "brown"]


#-----initialize turtle-----
ted = trtl.Turtle(shape = turtleshape)
ted.color(turtlecolor)
ted.shapesize(turtlesize)
ted.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-400, 300)
score_writer.ht()

font_setup = ("Arial", 30, "bold")
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.speed(0)
counter.ht()
counter.penup()
counter.goto(250,275)



#-----game functions--------
def ted_clicked(x,y):
    print("Ted got clicked")
    change_position()
    update_score()
    ted.color(random.choice(color_list))
    
def change_position():
    ted.penup()
    ted.ht()
    if not timer_up:
      tedx = random.randint(-400, 400)
      tedy = random.randint(-300, 300)
      ted.goto(tedx, tedy)
      ted.st()
      

def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Game Over", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global ted

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, ted, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, ted, score)

#-----events----------------

ted.onclick(ted_clicked)

wn = trtl.Screen()
wn.bgcolor("blue") # change the background color
wn.ontimer(countdown, counter_interval) 
wn.mainloop()