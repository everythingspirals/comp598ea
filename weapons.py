import ev3dev.ev3 as ev3

# motors
spinner = ev3.MediumMotor(ev3.OUTPUT_C)
hammer = ev3.LargeMotor(ev3.OUTPUT_D)

# hammer swings down until it hits something
# then swings back up until
def swing_hammer(speed_down, speed_up):
    hammer.reset()
    hammer.run_forever(speed_sp=speed_down)
    hammer.wait_until_not_moving()
    hammer.reset()
    hammer.run_forever(speed_sp=-speed_up)
    hammer.wait_until_not_moving()
    hammer.stop()

# start and stop rear weapon
def enable_spinner(speed):
    spinner.run_forever(speed_sp=speed)
def disable_spinner():
    spinner.stop()

def stop():
    spinner.stop(), hammer.stop()
