import turtle as t


robot_fn = "robotic_vacuum.gif"
rx = []
ry = []
move_cnt = 0

def move_robot(action):
    t.clear()
    if action == 0:
        for i in range(move_cnt):
            t.goto(rx[i], ry[i])
    elif action == 1:
        for i in range(move_cnt-1,-1,-1):
            t.goto(rx[i], ry[i])
    elif action == 2:
        t.goto(rx[move_cnt-1], ry[move_cnt-1])
    elif action == 3:
        t.goto(rx[0], ry[0])
    t.penup()
def clicked(x, y):
    global move_cnt
    move_cnt += 1
    rx.append(x)
    ry.append(y)
def list_clear():
    global move_cnt
    del rx[1:move_cnt]
    del ry[1:move_cnt]
    move_cnt = 1
        
def key_SP():
    move_robot(0)
def key_BS():
    move_robot(1)
def key_s():
    move_robot(2)
def key_r():
     move_robot(3)
def key_e():
    list_clear()
t.penup()
s = t.Screen()
t.hideturtle()

s.addshape(robot_fn)
t.shape(robot_fn)
t.speed(6)
t.penup()
clicked(-265, 265)
t.goto(-265, 265)
t.showturtle()

s.onkey(key_SP, "space")
s.onkey(key_BS, "BackSpace")
s.onkey(key_s, "s")
s.onkey(key_r, "r")
s.onkey(key_e, "e")
s.onscreenclick(clicked)
s.listen
