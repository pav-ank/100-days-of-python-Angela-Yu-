# In Reeborg's world
# Hurdle 3
Jumping over hurdles with variable heights
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdles():
    while wall_in_front() == True:
        turn_left()
        while wall_on_right():
            if front_is_clear() != True:
                turn_left()
            move()
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            move()


while not at_goal():
    if wall_in_front():
        hurdles()
    else:
        move()


# Hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear() and right_is_clear():
        move()
    else:
        turn_right()