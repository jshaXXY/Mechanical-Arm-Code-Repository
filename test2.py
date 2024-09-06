import servo
import servo_angle_2
import transfer

servo.servo_init()
r, theta = transfer.transfer_r_theta(376, 223)
servo.servo_angle(0, theta)

angle1, angle2, angle3 = servo_angle_2.servo_angles(r)
servo.servo_angle (3, angle3)
servo.servo_angle (2, angle2)
servo.servo_angle (1, angle1)