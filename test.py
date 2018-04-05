import ev3dev.ev3 as ev3
import robot as robot

# m = Motor(OUTPUT_A)
# n = Motor(OUTPUT_B)
# m.run_timed(time_sp=3000, speed_sp=500), n.run_timed(time_sp=3000, speed_sp=500)

# m = ev3.LargeMotor('outA')
# n = ev3.LargeMotor('outB')
# m.run_timed(time_sp=3000, speed_sp=500), n.run_timed(time_sp=3000, speed_sp=500)

robot.speak('I am alive')
# robot.swing(600,200)

robot.wheels.move_forward(600)
if(robot.touchSensor.is_pressed):
    robot.wheels.turn_left(600, 600, 200)
