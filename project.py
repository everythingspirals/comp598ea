import robot as robot

# main function not necessary but makes code cleaner
def main():
    # variables
    speed = 500

    # UltraSonicSensor distance
    distance = 20
    light = 10

    # Hammer swing strength
    swing_down = 700
    swing_up = 250

    # Spinner speed
    spin_speed = 300

    robot.speak('I am alive')
    while True:
        # search mode
        # while(robot.colorSensor.color != 'black' or
        #       robot.colorSensor.reflected_light_intensity > light):
        #     robot.wheels.move_forward(speed)
        #     if(robot.sonicSensor.distance_centimeters > distance or
        #             robot.touchSensor.is_pressed or
        #             not robot.wheels.running()):
        #         robot.wheels.move_forward(speed, speed, 200)

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