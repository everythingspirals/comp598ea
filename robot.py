import ev3dev.ev3 as ev3
import wheels as wheels
import weapons as weapons

distance = 20
light = 10

# sensors
# sensors have native boolean functions
sonicSensor = ev3.UltrasonicSensor(ev3.INPUT_1)
touchSensor = ev3.TouchSensor(ev3.INPUT_3)
colorSensor = ev3.ColorSensor(ev3.INPUT_4)

# input string for robot to say
def speak(String):
    ev3.Sound.speak(String).wait()

def stop():
    wheels.stop()
    weapons.stop()

def hasDot():
    return (colorSensor.color == 'black' or colorSensor.reflected_light_intensity > light)

def hasCollision():
    return (hasSight() or hasTouch())

def hasSight():
    return sonicSensor.distance_centimeters > distance

def hasTouch():
    return touchSensor.is_pressed