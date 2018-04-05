import ev3dev.ev3 as ev3
import time

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
def wait(duration):
    if (duration <= 0):
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

def move_wheels(l_speed, r_speed, duration=0):
    l_side.run_forever(speed_sp=l_speed),
    r_side.run_forever(speed_sp=r_speed)
    #time.sleep(2.0)
    wait(duration)
    #stop()
    #stop()

# movement functions
# wheels are inverted (spin in opposite directions)
# timer default is 0 (move forever
def move_forward(l_speed, r_speed, duration=0):
    move_wheels(l_speed, r_speed, duration)

def move_backward(l_speed, r_speed, duration=0):
    move_wheels(-l_speed, -r_speed, duration)

# turn functions
# wheels can spin at different speeds
# timer required to set turning radius
def turn_left(speed):
    move_wheels(speed, 0)

def turn_right(speed):
    move_wheels(0, speed)