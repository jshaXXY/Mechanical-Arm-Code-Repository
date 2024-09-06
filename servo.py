from adafruit_servokit import ServoKit
kit = ServoKit(channels = 16)

def servo_init():
    kit.servo[0].set_pulse_width_range(580, 2550)
    kit.servo[1].set_pulse_width_range(580, 2550)
    kit.servo[2].set_pulse_width_range(580, 2550)
    kit.servo[3].set_pulse_width_range(580, 2550)

def servo_angle(servoNum, angle):
    kit.servo[servoNum].angle = angle