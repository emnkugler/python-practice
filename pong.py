# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 15
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

#LEFT = True #change this?
#RIGHT = False

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-1, -1]
paddle1_pos = 40.0
paddle1_vel = 0.0
paddle2_pos = 40.0
paddle2_vel = 0.0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel # these are vectors stored as lists
    horiz_vel = random.randrange(120, 240)/60.0
    if direction == "LEFT":
        vel = [- random.randrange(1, 5),- random.randrange(1, 5)]
    else:
        vel = [random.randrange(1, 5),- random.randrange(1, 5)]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    spawn_ball(random.choice(["LEFT","RIGHT"]))
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    if paddle1_pos >= HEIGHT-40:
        paddle1_pos = HEIGHT-40
    elif paddle1_pos <= 40:
        paddle1_pos = 40
    if paddle2_pos >= HEIGHT-40:
        paddle2_pos = HEIGHT-40
    elif paddle2_pos <= 40:
        paddle2_pos = 40
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 2, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 2.5, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 2.5, "White")
    
    # draw paddles
    c.draw_line((0, paddle1_pos-40), (0, paddle1_pos + 40), 16, "Red")
    c.draw_line((WIDTH, paddle2_pos-40), (WIDTH, paddle2_pos+40), 16, "Blue")
    
    
    # update ball
    ball_pos[0] +=1*vel[0]
    ball_pos[1] +=1*vel[1]
    
    #top and bottom bounces
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    if ball_pos[1] >= (HEIGHT-1)-BALL_RADIUS:
        vel[1] = -vel[1]
    
    # check left gutter
    if ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        # check for paddle
        if paddle1_pos - HALF_PAD_HEIGHT - BALL_RADIUS <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT + BALL_RADIUS:
            # bounce
            ball_pos[0] = PAD_WIDTH + BALL_RADIUS
            vel[0] = - vel[0]
            vel[0] = 1.5*vel[0] # Increases velocity of ball
            vel[1] = 1.5*vel[1] # with each bounce off paddle
        else:
            #spawn_ball in center
            score2 +=1
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            spawn_ball("RIGHT")
    
    # check right gutter
    elif ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        # check for paddle
        if paddle2_pos - HALF_PAD_HEIGHT - BALL_RADIUS <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT + BALL_RADIUS:
            # bounce
            ball_pos[0] = WIDTH - PAD_WIDTH - BALL_RADIUS
            vel[0] = - vel[0]
            vel[0] = 1.1*vel[0]
            vel[1] = 1.1*vel[1]
        else:
            #spawn_ball in center
            score1 +=1
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            spawn_ball("LEFT")
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 5, "Yellow", "White")
    c.draw_text(str(score1), [WIDTH/4, 60], 50, "White")
    c.draw_text(str(score2), [WIDTH/1.4, 60], 50, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel-=4
    elif key == simplegui.KEY_MAP['S']:
        paddle1_vel+=4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel-=4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel+=4
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP['S']:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel=0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
Text= frame.add_label("Player 1: W = Up S = Down for Red/Left Paddle", 200)
Text= frame.add_label(" ")
Text = frame.add_label("Player 2: Arrow keys for Blue/Right Paddle", 200)
Text= frame.add_label(" ")
button1 = frame.add_button("Restart", new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
