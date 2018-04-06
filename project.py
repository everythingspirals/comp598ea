import robot as robot

# main function not necessary but makes code cleaner
def main():
    # variables
    speed = 800

    # UltraSonicSensor distance

    # Hammer swing strength
    swing_down = 700
    swing_up = 250

    # Spinner speed
    spin_speed = 300

    robot.speak('I am alive')
    robot.wheels.stop()

    while True:
        #search mode
        while(not robot.hasDot()):

            if(robot.hasTouch()):
                robot.speak('Collision detected')

            if(robot.hasSight()):
                robot.speak('I see you')

            #robot.wheels.move_forward(speed, speed)
            #robot.speak('I am alive')

            #if(robot.hasCollision()):
                #robot.wheels.move_forward(speed, speed, 200)
                #robot.wheels.move_forward(speed, speed)
                #robot.speak('Collision detected!')

        # # defense mode
        # while(robot.colorSensor.color == 'black' or
        #       robot.colorSensor.reflected_light_intensity < light):
        #     robot.wheels.stop()
        #     robot.weapons.enable_spinner(spin_speed)
        #     if(robot.sonicSensor.distance_centimeters > distance or
        #             robot.touchSensor.is_pressed):
        #         robot.weapons.swing_hammer(swing_down, swing_up)
        # robot.weapons.disable_spinner()

main() # run main program