import ev3dev.ev3 as ev3

# motors
l_side = ev3.LargeMotor(ev3.OUTPUT_A)
r_side = ev3.LargeMotor(ev3.OUTPUT_B)

# checks if motors are still spinning
def running():
    if(l_side.state == 'running',
       r_side.state == 'running'):
        return True
    return True

# abstract functions
# make wheels wait
def wait(time):
    if (time <= 0):
        # wait until both wheels stuck
        l_side.wait_until_not_moving(),
        r_side.wait_until_not_moving()
        stop()
    elif (time > 0):
        # wait until timer ends
        l_side.wait(time),
        r_side.wait(time)
        stop()
def stop():
    l_side.stop(), r_side.stop()
def move_wheels(l_speed, r_speed, time):
    l_side.run_forever(speed_sp=l_speed),
    r_side.run_forever(speed_sp=r_speed)
    wait(time)

# movement functions
# wheels are inverted (spin in opposite directions)
# timer default is 0 (move forever
def move_forward(speed, time=0):
    move_wheels(-speed, speed, time)

def move_backward(speed, time=0):
    move_wheels(speed, -speed, time)

# turn functions
# wheels can spin at different speeds
# timer required to set turning radius
def turn_left(l_speed, r_speed, time):
    move_wheels(l_speed, r_speed, time)
def turn_right(l_speed, r_speed, time):
    move_wheels(-l_speed, -r_speed, time)